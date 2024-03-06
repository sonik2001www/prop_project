import requests
import xml.etree.ElementTree as ET

url = "http://feed.bkkcondos.com/PropertyApi/DDProperty"

# Виконуємо запит до сторінки
response = requests.get(url)

# Перевіряємо, чи було успішне підключення
if response.status_code == 200:
    # Отримуємо текстовий вміст відповіді
    data = response.text

    # Розбір XML
    root = ET.fromstring(data)

    # Запис даних у новий файл
    output_file = 'новий_файл.xml'
    tree = ET.ElementTree(root)
    tree.write(output_file, encoding='utf-8', xml_declaration=True)
    print(f"Дані були успішно записані у файл: {output_file}")
else:
    print("Помилка при отриманні сторінки:", response.status_code)

