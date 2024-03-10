from math import radians, sin, cos, sqrt, atan2, floor

import requests

from config import API_KEY


def calculate_distance(lat1, lon1, lat2, lon2):
    # Функція для обчислення відстані між двома точками на земній поверхні
    R = 6371.0  # Середній радіус Землі в кілометрах

    lat1_rad = radians(lat1)
    lon1_rad = radians(lon1)
    lat2_rad = radians(lat2)
    lon2_rad = radians(lon2)

    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad

    a = sin(dlat / 2)**2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance


def find_condos_in_radius(average_latitude, average_longitude, condos, condos_all, radius):
    condos_in_radius = []

    # Знаходимо найвіддаленішу точку від центру
    farthest_distance = 0
    for condo in condos:
        distance = calculate_distance(average_latitude, average_longitude, float(condo.latitude), float(condo.longitude))
        if distance > farthest_distance:
            farthest_distance = distance

    # Розраховуємо відстань, яку маємо додати до радіусу
    total_radius = radius + farthest_distance

    # Проходимо по всім точкам і додаємо ті, які знаходяться в радіусі
    for condo in condos_all:
        distance = calculate_distance(average_latitude, average_longitude, float(condo.latitude), float(condo.longitude))
        if distance <= total_radius:
            condos_in_radius.append(condo)

    return condos_in_radius


def find_in_radius(condos, radius, places):

    print(len(condos))

    condos_in_radius = []

    for condo in condos:
        condo_lat, condo_lon = condo.latitude, condo.longitude
        found = False

        for place in places:
            place_lat, place_lon = place[1], place[2]
            distance = calculate_distance(float(condo_lat), float(condo_lon), place_lat, place_lon)

            if distance <= radius:
                found = True
                break

        if found:
            condos_in_radius.append(condo)

    print(len(condos_in_radius))
    return condos_in_radius


def get_coordinates(place):
    base_url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {
        'address': f'{place}, Bangkok',
        'key': API_KEY
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        latitude = location['lat']
        longitude = location['lng']
        return latitude, longitude
    return None


# Список шкіл
# Список шкіл

# schools_old = [
#     "American School of Bangkok",
#     "Ampornpaisarn School",
#     "Anglo Singapore International School",
#     "Assumption College (Thailand)",
#     "Assumption College Thonburi",
#     "Bangkok Christian College",
#     "Bangkok Christian International School",
#     "Bangkok Grace International School",
#     "Bangkok Patana School",
#     "Bangkok Preparatory International School",
#     "Bangpakok Wittayakom School",
#     "Bodindecha (Sing Singhaseni) School",
#     "Bromsgrove International School Thailand",
#     "Centurion International School Bangkok",
#     "Chitralada School",
#     "Concordian International School",
#     "Ekamai International School",
#     "Enconcept E-Academy",
#     "Garden International School Bangkok",
#     "Harrow International School, Bangkok",
#     "Heathfield International School",
#     "Horwang School",
#     "International Community School (Thailand)",
#     "International School Bangkok",
#     "Kasetsart University Laboratory School",
#     "KIS International School",
#     "Mater Dei School (Thailand)",
#     "Nawaminthrachinuthit Bodindecha School",
#     "New Sathorn International School",
#     "NIST International School",
#     "Niva International School",
#     "Pan-Asia International School",
#     "Patumwan Demonstration School, Srinakharinwirot University",
#     "Praht Thai School",
#     "Protpittayapayat School",
#     "Rajavinit Mathayom School",
#     "Ramkhamhaeng Advent International School",
#     "The Regent's School",
#     "Rittiyawannalai School",
#     "Ruamrudee International School",
#     "Sacred Heart Convent School (Bangkok)",
#     "Samsenwittayalai School",
#     "St Andrews International School Bangkok",
#     "Saint Gabriel's College",
#     "Saint John's Group of Schools",
#     "Saint John's International School (Thailand)",
#     "St. Mark's International School Bangkok",
#     "Sarasas Ektra School",
#     "Sarawittaya School",
#     "Satriwitthaya 2 School",
#     "Shrewsbury International School",
#     "Singapore International School of Bangkok",
#     "Traimitwitthayalai School",
#     "Suankularb Wittayalai School",
#     "Suksanari School",
#     "Taweethapisek School",
#     "Thai-Japanese Association School",
#     "Traill International School",
#     "Triam Udom Suksa Pattanakarn School",
#     "Triam Udom Suksa School",
#     "Triamudomsuksapattanakarn Ratchada School",
#     "Vajiravudh College",
#     "Wat Putthabucha School",
#     "Wat Suthiwararam School",
#     "Wattana Wittaya Academy",
#     "Wells International School",
#     "Yothinburana School"
# ]
#
# school_coordinates = []
#
# # Отримання координат для кожної школи
# for school in schools_old:
#     coordinates = get_coordinates(school)
#     if coordinates:
#         school_coordinates.append([school, coordinates[0], coordinates[1]])
#     else:
#         school_coordinates.append([school, None, None])
# # Виведення координат
# for school in school_coordinates:
#     print(school)

schools = [ ['American School of Bangkok', 13.7346846, 100.5758134],
            ['Ampornpaisarn School', 13.9256702, 100.5227032],
            ['Anglo Singapore International School', 13.6879703, 100.6090378],
            ['Assumption College (Thailand)', 13.7563309, 100.5017651],
            ['Assumption College Thonburi', 13.7320701, 100.3709888],
            ['Bangkok Christian College', 13.7207975, 100.523232],
            ['Bangkok Christian International School', 13.7342278, 100.6315207],
            ['Bangkok Grace International School', 13.7712605, 100.6167044],
            ['Bangkok Patana School', 13.663052, 100.6219206],
            ['Bangkok Preparatory International School', 13.7149999, 100.6015163],
            ['Bangpakok Wittayakom School', 13.6830631, 100.495063],
            ['Bodindecha (Sing Singhaseni) School', 13.7677464, 100.6148868],
            ['Bromsgrove International School Thailand', 13.8187359, 100.797328],
            ['Centurion International School Bangkok', 13.7052454, 100.6217094],
            ['Chitralada School', 13.7663794, 100.5227039],
            ['Concordian International School', 13.6382728, 100.6740613],
            ['Ekamai International School', 13.7308164, 100.5921479],
            ['Enconcept E-Academy', 13.7563309, 100.5017651],
            ['Garden International School Bangkok', 13.715204, 100.545965],
            ['Harrow International School, Bangkok', 13.9049799, 100.5834389],
            ['Heathfield International School', 13.7833437, 100.686121],
            ['Horwang School', 13.8187604, 100.5607702],
            ['International Community School (Thailand)', 13.6670036, 100.6518173],
            ['International School Bangkok', 13.7563309, 100.5017651],
            ['Kasetsart University Laboratory School', 13.8506313, 100.5684852],
            ['KIS International School', 13.7713099, 100.5891821],
            ['Mater Dei School (Thailand)', 13.7433489, 100.5431058],
            ['Nawaminthrachinuthit Bodindecha School', 13.7920236, 100.6065157],
            ['New Sathorn International School', 13.7012349, 100.5363066],
            ['NIST International School', 13.7467838, 100.5592757],
            ['Niva International School', 13.8024142, 100.6291464],
            ['Pan-Asia International School', 13.7032782, 100.6865583],
            ['Patumwan Demonstration School, Srinakharinwirot University', 13.7399015, 100.5346221],
            ['Praht Thai School', 13.7563309, 100.5017651],
            ['Protpittayapayat School', 13.726524, 100.784465],
            ['Rajavinit Mathayom School', 13.762619, 100.5149275],
            ['Ramkhamhaeng Advent International School', 13.7684494, 100.6583869],
            ["The Regent's School", 13.7674219, 100.59577],
            ['Rittiyawannalai School', 13.9131497, 100.6253628],
            ['Ruamrudee International School', 13.7838152, 100.7292359],
            ['Sacred Heart Convent School (Bangkok)', 13.7179479, 100.556434],
            ['Samsenwittayalai School', 13.7841575, 100.5344789],
            ['St Andrews International School Bangkok', 13.7243794, 100.5968223],
            ["Saint Gabriel's College", 13.7761955, 100.5070308],
            ["Saint John's Group of Schools", 13.7563309, 100.5017651],
            ["Saint John's International School (Thailand)", 13.809415, 100.5630008],
            ["St. Mark's International School Bangkok", 13.7408937, 100.6273838],
            ['Sarasas Ektra School', 13.6974702, 100.5296643],
            ['Sarawittaya School', 13.8511412, 100.5835256],
            ['Satriwitthaya 2 School', 13.8255189, 100.6171472],
            ['Shrewsbury International School', 13.709251, 100.510117],
            ['Singapore International School of Bangkok', 13.7704447, 100.6026044],
            ['Traimitwitthayalai School', 13.7384767, 100.5139846],
            ['Suankularb Wittayalai School', 13.7428163, 100.4987337],
            ['Suksanari School', 13.735199, 100.4956769],
            ['Taweethapisek School', 13.7447337, 100.4830717],
            ['Thai-Japanese Association School', 13.7608736, 100.5929639],
            ['Traill International School', 13.7513243, 100.6142789],
            ['Triam Udom Suksa Pattanakarn School', 13.7297371, 100.6477181],
            ['Triam Udom Suksa School', 13.7403853, 100.5306738],
            ['Triamudomsuksapattanakarn Ratchada School', 13.7728889, 100.5740032],
            ['Vajiravudh College', 13.7772609, 100.5175464],
            ['Wat Putthabucha School', 13.6509824, 100.4750642],
            ['Wat Suthiwararam School', 13.7126184, 100.5122486],
            ['Wattana Wittaya Academy', 13.744169, 100.560812],
            ['Wells International School', 13.7273221, 100.5770463],
            ['Yothinburana School', 13.8142251, 100.5200607]
        ]

# hospital_old = [
#     '430 Pitsanulok Rd, Dusit, Bangkok 10300, Thailand',
#     'No 80, Phatanavej 12, Pridi Banomyong 14, Sukhumvit 71, Bangkok, Thailand',
#     '9/1 Convent Road, Silom, Bangkok 10500, Thailand',
#     '430 Pitsanuloke Road, PO Box 613, Bangkok 10501, Thailand',
#     '2 Soi Soonvijai 7, New Petchburi Road, Bangkok 10310, Thailand',
#     '150 Moo 6, Tonmamoung subdistrict, Muang, Phetchaburi, Bangkok 76000, Thailand',
#     '1194 Phetchkesem Road, T.Sanamchan, A.Muang Nakhonpathon, Bangkok 73000, Thailand',
#     '98 Sukhumvit Soi 2, Khlong Toei, Ploench, Bangkok 10110, Thailand',
#     '33 Sukhumvit 3 (Soi Nana Nua), Wattana, Bangkok 10110, Thailand',
#     '113/44 Boromrachachonnee Road, Bangkoknoi, Bangkok 10700, Thailand',
#     '236/13 Praram 1 Road Pratoomone, Bangkok 10330, Thailand',
#     '17/41 Ramkhamhaeng 43/1 Road, Plubpla, Bangkok 10310, Thailand',
#     'Sukhumvit 68, Bangkok 10260, Thailand',
#     'Ploenchit center 2 Sukhumvit Rd, KlongToe, Bangkok 10110, Thailand',
#     'Sathornthane tower1, 1st FI, 90/7, Bangkok 10500, Thailand',
#     'BG037-039, 131/1, 141/1 The Shoppes grand, Bangkok 10310, Thailand',
#     '950 Prachachuen Road, Bangsue, Bangkok 10800, Thailand',
#     '1873 Rama 4 Road, Pathumwan, Bangkok 10330, Thailand',
#     '80, SOI Sangchan-Rubia, Prakanong, Bangkok 10100, Thailand',
#     'The Racquet Club 3rd Floor, Sukhumvit Soi 49/9, Wattana, Bangkok 10110, Thailand',
#     '670/1 Phaholyothin Rd, Samscnnai, Phayathai, Bangkok 10400, Thailand',
#     'Phyathai 2, 943, Phaholyothin Rd, Sam Sen Nai, Phaya Thai, Bangkok 10400, Thailand',
#     '44/505 Nawamin Road, Bunggoom, Bangkok 10230, Thailand',
#     '998 Rama 9 Road, Bangkapi, Huay-Kwang, Bangkok 10310, Thailand',
#     '99 Soi Praram 9 Hospital, Bangkok 10320, Thailand',
#     '436 Ramkhamhaeng, 34 Khwang Hua Mak Khet Bang Kapi, Bangkok 10240, Thailand',
#     '80/1 Sukhumvit 21 Road, Bangkok 10110, Thailand',
#     '215 South Sathorn Road, Bangkok 10120, Thailand',
#     '488 Srinakarin Road, Suanluang, Bangkok 10250, Thailand',
#     'Bangkok Hospital Chinatown, 624 Yaowarat Road, Sampantawong, Bangkok 10100, Thailand',
#     '133 Sukhumvit 49, Klong Tan Nua, Vadhana/Wattana, Bangkok 10110, Thailand',
#     '345 Bangna-Trad Highway, Bangna, Bangkok 10260, Thailand',
#     '611 Bamrung Muang Rd., Khlong Mahanak, Bangkok, Thailand',
#     '34/1 Issaraphap Rd., Soi 44, Ban-Changloh, Bangkok Noi, Bangkok 10700, Thailand',
#     '1 Ladprao Road 111, Klong-Chan Bangkapi, Bangkok 10240, Thailand',
#     '1 Tower, Floor 19, 888 Viphavadee-Rangsit Road, Chatuchak District, Bangkok 10900, Thailand',
#     '51/3 Ngamwongwan Rd, Jutujak, Bangkok 10900, Thailand',
#     '71/3 Setsiri Road, Phayathai, Bangkok 10400, Thailand',
#     '488 Srinakarin Road, Suanluang, Bangkok 10250, Thailand',
#     '80/1 Sukhumvit 21 Road, Bangkok 10110, Thailand'
# ]
#
# # Отримання координат для кожної школи
# for hospital in hospital_old:
#     coordinates = get_coordinates(hospital)
#     if coordinates:
#         hospital_coordinates.append([hospital, coordinates[0], coordinates[1]])
#     else:
#         hospital_coordinates.append([hospital, None, None])
#
# # Виведення координат
# for hospital in hospital_coordinates:
#     print(hospital)

hospitals = [['430 Pitsanulok Rd, Dusit, Bangkok 10300, Thailand', 13.766182, 100.5101418],
['No 80, Phatanavej 12, Pridi Banomyong 14, Sukhumvit 71, Bangkok, Thailand', 13.7196216, 100.5971255],
['9/1 Convent Road, Silom, Bangkok 10500, Thailand', 13.7249255, 100.5350638],
['430 Pitsanuloke Road, PO Box 613, Bangkok 10501, Thailand', 13.766182, 100.5101418],
['2 Soi Soonvijai 7, New Petchburi Road, Bangkok 10310, Thailand', 13.7461919, 100.5852513],
['150 Moo 6, Tonmamoung subdistrict, Muang, Phetchaburi, Bangkok 76000, Thailand', 13.7563309, 100.5017651],
['1194 Phetchkesem Road, T.Sanamchan, A.Muang Nakhonpathon, Bangkok 73000, Thailand', 13.8258993, 100.0630588],
['98 Sukhumvit Soi 2, Khlong Toei, Ploench, Bangkok 10110, Thailand', 13.737879, 100.5520396],
['33 Sukhumvit 3 (Soi Nana Nua), Wattana, Bangkok 10110, Thailand', 13.7466181, 100.553268],
['113/44 Boromrachachonnee Road, Bangkoknoi, Bangkok 10700, Thailand', 13.7548478, 100.4693893],
['236/13 Praram 1 Road Pratoomone, Bangkok 10330, Thailand', 13.8585083, 100.5865535],
['17/41 Ramkhamhaeng 43/1 Road, Plubpla, Bangkok 10310, Thailand', 13.7597976, 100.6165292],
['Sukhumvit 68, Bangkok 10260, Thailand', 13.6781365, 100.6024362],
['Ploenchit center 2 Sukhumvit Rd, KlongToe, Bangkok 10110, Thailand', 13.741573, 100.5514156],
['Sathornthane tower1, 1st FI, 90/7, Bangkok 10500, Thailand', 13.7262395, 100.5267991],
['BG037-039, 131/1, 141/1 The Shoppes grand, Bangkok 10310, Thailand', 13.7602517, 100.5684941],
['950 Prachachuen Road, Bangsue, Bangkok 10800, Thailand', 13.8319424, 100.5388405],
['1873 Rama 4 Road, Pathumwan, Bangkok 10330, Thailand', 13.7308701, 100.5355967],
['80, SOI Sangchan-Rubia, Prakanong, Bangkok 10100, Thailand', 13.7441095, 100.5099262],
['The Racquet Club 3rd Floor, Sukhumvit Soi 49/9, Wattana, Bangkok 10110, Thailand', 13.736351, 100.5762939],
['670/1 Phaholyothin Rd, Samscnnai, Phayathai, Bangkok 10400, Thailand', 13.7916325, 100.5509554],
['Phyathai 2, 943, Phaholyothin Rd, Sam Sen Nai, Phaya Thai, Bangkok 10400, Thailand', 13.7697436, 100.5406644],
['44/505 Nawamin Road, Bunggoom, Bangkok 10230, Thailand', 13.824697, 100.6573214],
['998 Rama 9 Road, Bangkapi, Huay-Kwang, Bangkok 10310, Thailand', 13.7523185, 100.5804386],
['99 Soi Praram 9 Hospital, Bangkok 10320, Thailand', 13.7530549, 100.5710193],
['436 Ramkhamhaeng, 34 Khwang Hua Mak Khet Bang Kapi, Bangkok 10240, Thailand', 13.75607, 100.6371964],
['80/1 Sukhumvit 21 Road, Bangkok 10110, Thailand', 13.7393651, 100.5569053],
['215 South Sathorn Road, Bangkok 10120, Thailand', 13.7194185, 100.5244701],
['488 Srinakarin Road, Suanluang, Bangkok 10250, Thailand', 13.7487903, 100.6380215],
['Bangkok Hospital Chinatown, 624 Yaowarat Road, Sampantawong, Bangkok 10100, Thailand', 13.737828, 100.512612],
['133 Sukhumvit 49, Klong Tan Nua, Vadhana/Wattana, Bangkok 10110, Thailand', 13.7348727, 100.5765805],
['345 Bangna-Trad Highway, Bangna, Bangkok 10260, Thailand', 13.671705, 100.6164136],
['611 Bamrung Muang Rd., Khlong Mahanak, Bangkok, Thailand', 13.7506001, 100.5145726],
['34/1 Issaraphap Rd., Soi 44, Ban-Changloh, Bangkok Noi, Bangkok 10700, Thailand', 13.752726, 100.4798742],
['1 Ladprao Road 111, Klong-Chan Bangkapi, Bangkok 10240, Thailand', 13.8089628, 100.6202445],
['1 Tower, Floor 19, 888 Viphavadee-Rangsit Road, Chatuchak District, Bangkok 10900, Thailand', 13.8269447, 100.5570612],
['51/3 Ngamwongwan Rd, Jutujak, Bangkok 10900, Thailand', 13.8455291, 100.5646908],
['71/3 Setsiri Road, Phayathai, Bangkok 10400, Thailand', 13.7806121, 100.5318636],
['488 Srinakarin Road, Suanluang, Bangkok 10250, Thailand', 13.7487903, 100.6380215],
['80/1 Sukhumvit 21 Road, Bangkok 10110, Thailand', 13.7393651, 100.5569053]]


def change_price(currency_switcher_value,  condos):
    new_condos = []

    all_kof = {
        "US": 1 / 3.67,
        "AED": 1,
        "EUR": 1 / 4.32,
        "JPY": 1 / 0.034,
        "GBP": 1 / 4.86,
        "AUD": 1 / 2.68,
        "CAD": 1 / 2.93,
        "CHF": 1 / 3.98,
        "CNY": 1 / 0.57,
        "HKD": 1 / 0.47,
        "NZD": 1 / 2.45,
        "SEK": 1 / 0.41,
        "KRW": 1 / 0.0032,
        "SGD": 1 / 2.71,
        "NOK": 1 / 0.42,
        "MXN": 1 / 0.18,
        "INR": 1 / 0.049,
        "BRL": 1 / 0.68,
        "RUB": 1 / 0.05,
        "ZAR": 1 / 0.26,
        "TRY": 1 / 0.41,
        "PLN": 1 / 0.96,
        "CZK": 1 / 0.17,
        "THB": 1 / 0.11,
        "IDR": 1 / 0.00026,
        "HUF": 1 / 0.011,
        "DKK": 1 / 0.58,
        "ILS": 1 / 1.14,
        "PHP": 1 / 0.068,
        "MYR": 1 / 0.88,
        'None': 1,
    }

    kof = all_kof[f"{currency_switcher_value}"]

    print(kof, currency_switcher_value)

    for condo in condos:

        if condo.sold_price:
            # try:
            condo.sold_price = convert_price(kof, condo.sold_price, currency_switcher_value)

        if condo.rent_price:
            # try:
            condo.rent_price = convert_price(kof, condo.rent_price, currency_switcher_value)
        new_condos.append(condo)

    return new_condos


def convert_price(kof, price, currency_switcher_value):

    converted_price = float(price) * kof

    formatted_price = format_price(converted_price)

    return formatted_price + f' {currency_switcher_value}'


def format_price(price):
    suffixes = ['', 'k', 'm', 'b', 't']
    suffix_index = 0
    while price >= 1000 and suffix_index < len(suffixes):
        price /= 1000
        suffix_index += 1
    formatted_price = '{:.1f}{}'.format(floor(price * 10) / 10, suffixes[suffix_index])
    return formatted_price


def save_change_price(request, lists, not_user, condos):
    # збереження для авторизованих користувачів валюти
    if request.method == 'POST' and request.user.is_authenticated:
        switcher = request.POST.get('CurrencySwitcher', '')
        lists.currency_switcher = str(switcher)
        lists.save()

    # зміна цін для авторизованих користувачів
    if request.user.is_authenticated:
        condos = change_price(lists.currency_switcher, condos)

    # збереження ціни для неавторизованих користувачів
    if request.method == 'POST' and not request.user.is_authenticated:
        switcher = request.POST.get('CurrencySwitcher', '')
        not_user.currency_switcher = str(switcher)
        not_user.save()

    # зміна цін для неавторизованих користувачів
    if not request.user.is_authenticated:
        condos = change_price(not_user.currency_switcher, condos)

    return condos