import re
import xml.etree.ElementTree as ET

from load_django import *
from property.models import *

# Відкриваємо файл XML
tree = ET.parse('новий_файл.xml')
root = tree.getroot()

# Ітеруємося по кожному елементу "property"
for property_elem in root.iter('property'):
    defaults = {}

    project_instance = Project.objects.get(project_name="Test Project")

    # Отримуємо дані про нерухомість
    property_id = property_elem.find('external-id').text
    property_name = property_elem.find('location/property-name').text
    property_description = property_elem.find('details/description').text

    # Виводимо дані про нерухомість
    # print("Property ID:", property_id)
    # print("Property Name:", property_name)
    # print("Property Description:", property_description)

    defaults['condo_name'] = property_name
    defaults['description'] = property_description

    # Інші поля нерухомості
    location = property_elem.find('location')

    # streetname = location.find('streetname').text
    # streetnumber = location.find('streetnumber').text
    # post_code = location.find('post-code').text
    # area_code = location.find('area-code').text
    # district_code = location.find('district-code').text

    property_type = location.find('property-type-group').text

    if property_type == 'N':
        defaults['property_type'] = 'Condo'
    elif property_type == 'B':
        defaults['property_type'] = 'House'

    longitude = location.find('longitude').text
    latitude = location.find('latitude').text

    defaults['longitude'] = longitude
    defaults['latitude'] = latitude

    details = property_elem.find('details')

    features = str(details.find('features').text)
    amenities = str(details.find('amenities').text)

    if len(features) > 2 and len(amenities) > 2 and amenities != "None" and features != "None":
        defaults['property_features'] = ", ".join([i.capitalize() for i in (features + ',' + amenities).split(",")])
    elif len(features) > 2 and features != "None":
        defaults['property_features'] = ", ".join([i.capitalize() for i in features.split(",")])
    elif len(amenities) > 2 and amenities != "None":
        defaults['property_features'] = ", ".join([i.capitalize() for i in amenities.split(",")])

    price_details = details.find('price-details')

    rooms = details.find('rooms')
    num_bedrooms = rooms.find('num-bedrooms').text
    num_bathrooms = rooms.find('num-bathrooms').text

    defaults['bedrooms'] = num_bedrooms
    defaults['bathrooms'] = num_bathrooms

    furnishing = details.find('furnishing').text
    if str(furnishing) == "UNFUR":
        defaults['bathrooms'] = 'Unfurnished'
    elif str(furnishing) == "FULL":
        defaults['bathrooms'] = 'Fully Furnished'

    size_details = details.find('size-details')
    floor_area = size_details.find('floor-area').text

    if str(size_details.find('land-area').text[4:]) != "0":
        land_area = size_details.find('land-area').text[4:]
        defaults['land_size'] = land_area

    defaults['property_size'] = floor_area

    parking_spaces = details.find('parking-spaces').text
    number_of_floors = details.find('numberoffloors').text
    floor_level = details.find('floor-level').text

    defaults['num_of_parking_spaces'] = parking_spaces
    defaults['floor_number'] = number_of_floors
    defaults['num_of_storeys'] = floor_level

    listing_type = property_elem.find('listing-type').text

    if listing_type == "RENT":
        defaults['listing_type'] = "Rent"
        defaults['rent_price'] = price_details.find('price').text

    if listing_type == "SALE":
        defaults['listing_type'] = "Sell"
        defaults['sold_price'] = price_details.find('price').text

    photos_list = property_elem.findall("photo/picture-url")
    photos_list = [i.text for i in photos_list]
    photos_list = list(set(photos_list))  # Видалення дублікатів
    photos_list.sort(key=lambda x: int(re.search(r'\((\d+)\)', x).group(1)) if re.search(r'\((\d+)\)', x) else 0)
    photos = ",,".join(photos_list)

    defaults["photo_links"] = photos
    # Виводимо інші поля нерухомості

    # print("Features:", features)
    #
    # print("Number of Bedrooms:", num_bedrooms)
    #
    # print("Number of Bathrooms:", num_bathrooms)
    # print("Furnishing:", furnishing)
    # print("Floor Area:", floor_area)
    #
    # print("Land Area:", land_area)
    # print("Parking Spaces:", parking_spaces)
    # print("Number of Floors:", number_of_floors)
    # print("Floor Level:", floor_level)
    #
    # print("Listing Type:", listing_type)

    print(defaults)

    try:
        prop = Property.objects.get(external_property_id=property_id)
        prop.listing_type = 'Sell&Rent'

        prop.rent_price = defaults['rent_price']
        prop.save()
    except:
        obj, created = Property.objects.get_or_create(
            external_property_id=property_id,
            project=project_instance,
            defaults=defaults,
        )

    print("-" * 30)

