import requests
from bs4 import BeautifulSoup

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

    # Проходимося по кожному елементу "item"
    for item in items:
        try:
            project_name = str(item.find('projectName').get_text())

            overview_instance = Overview.objects.get(name_overview=str(item.find('freeformLocation').get_text()))
            developer_instance = Developer.objects.get(id=2)

            obj, created = Project.objects.get_or_create(
                project_name=project_name,
                developer=developer_instance,
                overview_key=overview_instance,
            )
            print("ok")
        except:
            pass

else:
    print("Помилка при отриманні сторінки:", response.status_code)
