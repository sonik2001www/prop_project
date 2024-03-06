import requests
from bs4 import BeautifulSoup
import re

from .load_django import *
from property.models import *
from django.contrib.auth.models import User


def parsing(username, url):

    try:

        response = requests.get(url)

        xml_content = response.content
        soup = BeautifulSoup(xml_content, "lxml-xml")

        items = soup.find_all("item")

        data = []
        for item in items:
            defaults = {}

            try:
                name_overview = str(item.find('freeformLocation').get_text())

                obj, created = Overview.objects.get_or_create(
                    name_overview=name_overview.strip(),
                )
                print("ok")
            except:
                pass

            try:
                project_name = str(item.find('projectName').get_text())

                overview_instance = Overview.objects.get(name_overview=str(item.find('freeformLocation').get_text()).strip())
                developer_instance = Developer.objects.get(developer_name="Test Developer")

                obj, created = Project.objects.get_or_create(
                    project_name=project_name.strip(),
                    developer=developer_instance,
                    overview_key=overview_instance,
                )
                print("ok")
            except:
                pass

            property_name = str(item.find('title').get_text())
            defaults['description'] = str(item.find('description').get_text())
            try:
                project_instance = Project.objects.get(project_name=str(item.find('projectName').get_text()).strip(), overview_key=overview_instance)
            except:
                try:
                    project_instance = Project.objects.get(project_name=str(item.find('projectName').get_text()).strip())
                except:
                    project_instance = Project.objects.get(project_name="Test Project")
            defaults['property_type'] = str(item.find('propertyType').get_text()).capitalize()
            defaults['external_property_id'] = str(item.find('refId').get_text())
            defaults['location'] = str(item.find('region').get_text())
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
            map_latitude = str(item.find('lat').get_text())
            map_longitude = str(item.find('lng').get_text())

            user_instance = User.objects.get(username=username)

            obj, created = Property.objects.get_or_create(
                property_name=property_name.strip(),
                project=project_instance,
                photo_links=photos,
                latitude=map_latitude,
                longitude=map_longitude,
                agent=user_instance,
                defaults=defaults,
            )

    except:
        print("Помилка при отриманні сторінки")
