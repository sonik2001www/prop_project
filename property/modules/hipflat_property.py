import requests
from bs4 import BeautifulSoup
import re

from load_django import *
from property.models import *

url = "http://feed.bkkcondos.com/api/propertyapi/HipflatRSS"

# Виконуємо запит до сторінки
response = requests.get(url)

# Перевіряємо, чи було успішне підключення
if response.status_code == 200:
    # Отримуємо XML-код сторінки
    xml_content = response.content

    # Створюємо об'єкт BeautifulSoup для розбору XML-коду з використанням lxml-парсера
    soup = BeautifulSoup(xml_content, "lxml-xml")

    # Знаходимо всі елементи з тегом "item"
    items = soup.find_all("item")

    # Створюємо список для збереження витягнутих даних
    data = []

    # Проходимося по кожному елементу "item" і отримуємо текстовий вміст
    for item in items:
        defaults = {}

        condo_name = str(item.find('title').get_text())
        defaults['description'] = str(item.find('description').get_text())
        # defaults['aaa'] = str(item.find('link').get_text())
        # defaults['aaa'] = str(item.find('status').get_text())
        try:
            project_instance = Project.objects.get(project_name=str(item.find('projectName').get_text()))
        except:
            project_instance = Project.objects.get(project_name="Test Project")
        defaults['property_type'] = str(item.find('propertyType').get_text()).capitalize()
        defaults['external_property_id'] = str(item.find('refId').get_text())
        # defaults['aaa'] = str(item.find('published').get_text())
        # defaults['aaa'] = str(item.find('updated').get_text())
        defaults['location'] = str(item.find('region').get_text())
        # try:
        #     defaults['aaa'] = str(item.find('freeformLocation').get_text())
        # except:
        #     pass
        try:
            defaults['sold_price'] = str(item.find('salePrice').get_text())
            defaults['rent_price'] = str(item.find('rentPrice').get_text())

            defaults['listing_type'] = 'Sell&Rent'
        except:
            try:
                defaults['sold_price'] = str(item.find('salePrice').get_text())
                defaults['listing_type'] = 'Sell'
            except:
                pass
            try:
                defaults['rent_price'] = str(item.find('rentPrice').get_text())
                defaults['listing_type'] = 'Rent'
            except:
                pass

        defaults['bedrooms'] = str(item.find('beds').get_text())
        defaults['bathrooms'] = str(item.find('baths').get_text())
        defaults['property_size'] = str(int(float(item.find('area').get_text())))
        try:
            defaults['floor_number'] = str(item.find('floor').get_text())
        except:
            pass

        photos_list = [i.get_text() for i in item.find_all('photo')]
        photos_list = list(set(photos_list))  # Видалення дублікатів
        photos_list.sort(key=lambda x: int(re.search(r'\((\d+)\)', x).group(1)) if re.search(r'\((\d+)\)', x) else 0)

        photos = ",,".join(photos_list)

        features = item.find('features')
        features_str = ''
        if features is not None:
            feature_names = [feature.name.capitalize() for feature in features.find_all(lambda tag: tag.text == '1')]
            features_str = ', '.join(feature_names)

        defaults['property_features'] = features_str

        # vendor = item.find('vendorDetails')
        # defaults['aaa'] = str(vendor.find('name').get_text())
        # defaults['aaa'] = str(vendor.find('phone').get_text())
        # defaults['aaa'] = str(vendor.find('email').get_text())
        # defaults['aaa'] = str(vendor.find('lineID').get_text())

        map_latitude = str(item.find('lat').get_text())
        map_longitude = str(item.find('lng').get_text())

        # print(latitude, longitude)

        obj, created = Property.objects.get_or_create(
            condo_name=condo_name,
            project=project_instance,
            photo_links=photos,
            latitude=map_latitude,
            longitude=map_longitude,
            defaults=defaults,
        )



    # # Виводимо отримані дані
    # for item_data in data:
    #     print(item_data)
else:
    print("Помилка при отриманні сторінки:", response.status_code)
