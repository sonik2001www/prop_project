import os
import asyncio
from .aditional import *

import requests
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import UpdateView
from django.shortcuts import render, redirect
from .forms import ContactForm, PropertyForm
from .models import *
from django.core.paginator import Paginator
from .tasks import start_parsing
from datetime import date, timedelta
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.urls import reverse


async def http_call_async_pars_url(username, url):
    await start_parsing(username, url)


async def pars_url(username, url):
    loop = asyncio.get_event_loop()
    await loop.create_task(http_call_async_pars_url(username, url))
    return redirect('index')


async def parsing(request):
    if request.method == 'POST':
        data = request.POST.get('input_data')
        username = request.user
        await pars_url(username, data)
        print(username, data)
    return render(request, 'agent/parsing.html')


def agent_overviews(request):
    username = request.user
    user_instance = User.objects.get(username=username)
    overviews_list = Overview.objects.filter(project__property__agent=user_instance).distinct().order_by('pk')[::-1]

    len_developers = len(overviews_list)

    paginator = Paginator(overviews_list, 15)  # Вказуємо кількість елементів на сторінку
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    first_index = page_obj.start_index() if page_obj else None
    last_index = page_obj.end_index() if page_obj else None
    return render(request, 'agent/overviews.html', locals())


def agent_projects(request):
    page = None
    username = request.user
    user_instance = User.objects.get(username=username)
    projects_list = Project.objects.filter(property__agent=user_instance).distinct().order_by('pk')[::-1]

    len_developers = len(projects_list)

    if request.method == 'POST':
        page = request.POST.get('page')
        for key, value in request.POST.items():
            if key.isdigit():
                project_id = key
                project = Project.objects.get(pk=int(project_id))
                if 'on' in value:
                    properties = Property.objects.filter(project=project.pk)
                    for prop in properties:
                        prop.status = True
                        prop.save()
                    project.status = True
                else:
                    properties = Property.objects.filter(project=project.pk)
                    for prop in properties:
                        prop.status = False
                        prop.save()
                    project.status = False
                project.save()

    paginator = Paginator(projects_list, 15)  # Вказуємо кількість елементів на сторінку
    page_number = request.GET.get('page')
    if page is None:
        page_number = request.GET.get('page')
    else:
        page_number = page
    page_obj = paginator.get_page(page_number)

    first_index = page_obj.start_index() if page_obj else None
    last_index = page_obj.end_index() if page_obj else None
    return render(request, 'agent/projects.html', locals())


def agent_properties(request, items_per_page=15, sort_order=None):

    page = None
    search_pk = request.GET.get('search_pk')
    search_external_id = request.GET.get('search_external_id')

    if request.method == 'POST':
        page = request.POST.get('page')
        items_per_page_and_sort_order = str(request.POST.get('items_per_page-sort_order')).split("&")
        print(items_per_page_and_sort_order)
        items_per_page = items_per_page_and_sort_order[0]
        try:
            sort_order = items_per_page_and_sort_order[1]
        except:
            pass

        for key, value in request.POST.items():
            if key.isdigit():
                property_id = key
                prop = Property.objects.get(pk=int(property_id))
                if 'on' in value:
                    prop.status = True
                else:
                    prop.status = False
                prop.save()

    username = request.user
    user_instance = User.objects.get(username=username)

    properties_list = Property.objects.order_by('-pk').filter(agent=user_instance)
    if sort_order == 'asc':
        properties_list = properties_list.order_by('pk')
    elif sort_order == 'desc':
        properties_list = properties_list.order_by('-pk')
    elif sort_order == 'external_property_id_asc':
        properties_list = properties_list.order_by('external_property_id')
    elif sort_order == 'external_property_id_desc':
        properties_list = properties_list.order_by('-external_property_id')
    elif sort_order == 'property_name_asc':
        properties_list = properties_list.order_by('property_name')
    elif sort_order == 'property_name_desc':
        properties_list = properties_list.order_by('-property_name')
    elif sort_order == 'project__project_name_asc':
        properties_list = properties_list.order_by('project__project_name')
    elif sort_order == 'project__project_name_desc':
        properties_list = properties_list.order_by('-project__project_name')
    elif sort_order == 'project__overview_key__name_overview_asc':
        properties_list = properties_list.order_by('project__overview_key__name_overview')
    elif sort_order == 'project__overview_key__name_overview_desc':
        properties_list = properties_list.order_by('-project__overview_key__name_overview')
    elif sort_order == 'sold_price_asc':
        properties_list = properties_list.order_by('sold_price')
    elif sort_order == 'sold_price_desc':
        properties_list = properties_list.order_by('-sold_price')
    elif sort_order == 'rent_price_asc':
        properties_list = properties_list.order_by('rent_price')
    elif sort_order == 'rent_price_desc':
        properties_list = properties_list.order_by('-rent_price')
    elif sort_order == 'bedrooms_asc':
        properties_list = properties_list.order_by('bedrooms')
    elif sort_order == 'bedrooms_desc':
        properties_list = properties_list.order_by('-bedrooms')
    elif sort_order == 'bathrooms_asc':
        properties_list = properties_list.order_by('bathrooms')
    elif sort_order == 'bathrooms_desc':
        properties_list = properties_list.order_by('-bathrooms')
    elif sort_order == 'property_size_asc':
        properties_list = properties_list.order_by('property_size')
    elif sort_order == 'property_size_desc':
        properties_list = properties_list.order_by('-property_size')

    if search_pk:
        properties_list = properties_list.filter(pk=search_pk)
    if search_external_id:
        properties_list = properties_list.filter(external_property_id=search_external_id)

    len_developers = len(properties_list)

    paginator = Paginator(properties_list, items_per_page)
    if page is None:
        page_number = request.GET.get('page')
    else:
        page_number = page
    page_obj = paginator.get_page(page_number)

    first_index = page_obj.start_index() if page_obj else None
    last_index = page_obj.end_index() if page_obj else None

    return render(request, 'agent/properties.html', locals())


def property_create(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agent_properties')
    else:
        form = PropertyForm()
    return render(request, 'agent/property_create.html', {'form': form})


class PropertyUpdateView(UpdateView):
    model = Property
    form_class = PropertyForm
    template_name = 'agent/property_update.html'
    success_url = '/agent/properties/'


#
def creation(request):

    project_names = list(Project.objects.values_list('project_name', flat=True))

    form_num = request.FILES

    if request.method == 'POST':

        # page_1
        property_type = request.POST.get('propertyType')
        ptypes = request.POST.get('ptypes')
        name = request.POST.get('NextId1Name')
        region = request.POST.get('region')
        location = request.POST.get('location')
        subdistrict = request.POST.get('subdistrict')
        street_address = request.POST.get('streetAddress')

        # page_3
        count_bed = request.POST.get('count-bed')
        count_bath = request.POST.get('count-bath')
        property_size = request.POST.get('NextId3propertySize')
        outdoor_area_size = request.POST.get('NextId3outdoorAreaSize')
        land_size = request.POST.get('NextId3landSize')
        select_storeys = request.POST.get('selectStoreys')
        select_year = request.POST.get('selectYear')
        select_month = request.POST.get('selectMounth')

        # page_4
        furnishing = request.POST.get('furnishing')
        num_of_parking_spaces = request.POST.get('num_of_parking_spaces')
        pets_allowed = request.POST.get('pets_allowed')

        foreign_ownership = request.POST.get('foreignOwnership')
        thai_ownership = request.POST.get('thaiOwnership')
        leasehold = request.POST.get('leasehold')
        company = request.POST.get('company')

        company_land = request.POST.get('company_land')
        thai_ownership_land = request.POST.get('thaiOwnership_land')
        leasehold_land = request.POST.get('leasehold_land')

        title_deed = request.POST.get('title_deed')
        buy_select_year = request.POST.get('buySelectYear')
        buy_select_mounth = request.POST.get('buySelectMounth')

        # page 5
        # Outdoor Features
        media_room_cinema = request.POST.get('mediaRoomCinema')
        private_gym = request.POST.get('privateGym')
        private_lift = request.POST.get('privateLift')
        private_sauna = request.POST.get('privateSauna')
        jacuzzi = request.POST.get('jacuzzi')
        bathtub = request.POST.get('bathtub')
        fully_renovated = request.POST.get('fullyRenovated')
        date_fully_renovated = request.POST.get('dateFullyRenovated')

        corner_unit = request.POST.get('cornerUnit')
        maids_quarters = request.POST.get('maidsQuarters')
        duplex = request.POST.get('duplex')
        balcony = request.POST.get('balcony')
        full_western_kitchen = request.POST.get('fullWesternKitchen')
        renovated_kitchen = request.POST.get('renovatedKitchen')
        date_renovated_kitchen = request.POST.get('dateRenovatedKitchen')

        renovated_bathroom = request.POST.get('renovatedBathroom')
        date_renovated_bathroom = request.POST.get('dateRenovatedBathroom')

        # Rental Features
        private_pool = request.POST.get('privatePool')
        pool_access = request.POST.get('poolAccess')
        rooftop_terrace = request.POST.get('rooftopTerrace')
        private_garden = request.POST.get('privateGarden')
        garden_access = request.POST.get('gardenAccess')
        terrace = request.POST.get('terrace')
        covered_parking = request.POST.get('coveredParking')
        outdoor_showers = request.POST.get('outdoorShowers')

        # Location Features
        beachfront = request.POST.get('beachfront')
        beach_access = request.POST.get('beachAccess')
        oceanfront = request.POST.get('oceanfront')
        ocean_access = request.POST.get('oceanAccess')

        # What are the views of your property?
        blocked_view = request.POST.get('blockedView')
        unblocked_open_view = request.POST.get('unblockedOpenView')
        city_view = request.POST.get('cityView')
        river_canal_view = request.POST.get('riverCanalView')
        pool_view = request.POST.get('poolView')
        garden_view = request.POST.get('gardenView')
        park_view = request.POST.get('parkView')
        sea_view = request.POST.get('seaView')
        partial_sea_view = request.POST.get('partialSeaView')
        lake_view = request.POST.get('lakeView')
        mountain_view = request.POST.get('mountainView')
        golf_course_view = request.POST.get('golfCourseView')

        # step_2 page_1
        chose_images_main = request.FILES.getlist('choseImagesMain')
        chose_image = request.FILES.getlist('choseImage')

        # step_2 page_2
        chose_image_plan = request.FILES.getlist('choseImagePlan')

        # step_2 page_3
        listing = request.POST.get('NextId3step2Listing')
        description = request.POST.get('NextId3step2Description')

        # step_3 page_1
        rental_status = request.POST.get('available')
        date_available = request.POST.get('dateAvailableAfterThisDate')
        rental_duration = request.POST.get('rentalDuration')

        # step_3 page_2
        year = request.POST.get('NextId3step3Year')
        month_3_6 = request.POST.get('NextId3step3Listing3_6Month')
        month = request.POST.get('NextId3step3ListingMonth')

        # step_3 page_3
        keys = request.POST.get('keys')
        key_1_first_name = request.POST.get('key_1_first_name')
        key_1_last_name = request.POST.get('key_1_last_name')
        key_1_phone = request.POST.get('key_1_phone')
        key_1_email = request.POST.get('key_1_email')
        key_1_message = request.POST.get('key_1_message')
        key_2_first_name = request.POST.get('key_2_first_name')
        key_2_last_name = request.POST.get('key_2_last_name')
        key_2_phone = request.POST.get('key_2_phone')
        key_2_email = request.POST.get('key_2_email')
        key_2_message = request.POST.get('key_2_message')
        key_5_message = request.POST.get('key_5_message')

        phone = request.POST.get("NextId3step3Year")
        i_am = request.POST.get("i_am")

        # page_1
        print('property_type:', property_type)
        print('ptypes:', ptypes)
        print('name:', name)
        print('region:', region)
        print('location:', location)
        print('subdistrict:', subdistrict)
        print('street_address:', street_address)

        # page_2
        print('count_bed:', count_bed)
        print('count_bath:', count_bath)
        print('property_size:', property_size)
        print('outdoor_area_size:', outdoor_area_size)
        print('land_size:', land_size)

        # page_3
        print('select_storeys:', select_storeys)
        print('select_year:', select_year)
        print('select_month:', select_month)
        print('furnishing:', furnishing)
        print('num_of_parking_spaces:', num_of_parking_spaces)
        print('pets_allowed:', pets_allowed)

        # page_4
        print('select_storeys:', select_storeys)
        print('select_year:', select_year)
        print('select_month:', select_month)
        print('furnishing:', furnishing)
        print('num_of_parking_spaces:', num_of_parking_spaces)
        print('pets_allowed:', pets_allowed)
        print('foreign_ownership:', foreign_ownership)
        print('thai_ownership:', thai_ownership)
        print('leasehold:', leasehold)
        print('company:', company)
        print('company_land:', company_land)
        print('thai_ownership_land:', thai_ownership_land)
        print('leasehold_land:', leasehold_land)
        print('title_deed:', title_deed)
        print('buy_select_year:', buy_select_year)
        print('buy_select_mounth:', buy_select_mounth)

        # page_5
        print('media_room_cinema:', media_room_cinema)
        print('private_gym:', private_gym)
        print('private_lift:', private_lift)
        print('private_sauna:', private_sauna)
        print('jacuzzi:', jacuzzi)
        print('bathtub:', bathtub)
        print('fully_renovated:', fully_renovated)
        print('date_fully_renovated:', date_fully_renovated)
        print('corner_unit:', corner_unit)
        print('maids_quarters:', maids_quarters)
        print('duplex:', duplex)
        print('balcony:', balcony)
        print('full_western_kitchen:', full_western_kitchen)
        print('renovated_kitchen:', renovated_kitchen)
        print('date_renovated_kitchen:', date_renovated_kitchen)
        print('renovated_bathroom:', renovated_bathroom)
        print('date_renovated_bathroom:', date_renovated_bathroom)
        print('private_pool:', private_pool)
        print('pool_access:', pool_access)
        print('rooftop_terrace:', rooftop_terrace)
        print('private_garden:', private_garden)
        print('garden_access:', garden_access)
        print('terrace:', terrace)
        print('covered_parking:', covered_parking)
        print('outdoor_showers:', outdoor_showers)
        print('beachfront:', beachfront)
        print('beach_access:', beach_access)
        print('oceanfront:', oceanfront)
        print('ocean_access:', ocean_access)
        print('blocked_view:', blocked_view)
        print('unblocked_open_view:', unblocked_open_view)
        print('city_view:', city_view)
        print('river_canal_view:', river_canal_view)
        print('pool_view:', pool_view)
        print('garden_view:', garden_view)
        print('park_view:', park_view)
        print('sea_view:', sea_view)
        print('partial_sea_view:', partial_sea_view)
        print('lake_view:', lake_view)
        print('mountain_view:', mountain_view)
        print('golf_course_view:', golf_course_view)

        # step_2 page_1
        print(chose_images_main)
        print(chose_image)

        # step_2 page_2
        print(chose_image_plan)

        # step_2 page_3
        print("listing:", listing)
        print("description:", description)

        # step_3 page_1
        print("rental_status:", rental_status)
        print("date_available:", date_available)
        print("rental_duration:", rental_duration)

        # step_3 page_2
        print("year:", year)
        print("month_3_6:", month_3_6)
        print("month:", month)

        # step_3 page_3
        print("keys:", keys)
        print("key_1_first_name:", key_1_first_name)
        print("key_1_last_name:", key_1_last_name)
        print("key_1_phone:", key_1_phone)
        print("key_1_email:", key_1_email)
        print("key_1_message:", key_1_message)
        print("key_2_first_name:", key_2_first_name)
        print("key_2_last_name:", key_2_last_name)
        print("key_2_phone:", key_2_phone)
        print("key_2_email:", key_2_email)
        print("key_2_message:", key_2_message)
        print("key_5_message:", key_5_message)

    return render(request, 'creation.html', {'form_num': form_num, 'project_names': project_names})


#
def property_details(request, property_id):
    property = Property.objects.get(id=property_id)
    return render(request, 'property_details.html', {'property': property})


#
def properties(request):
    properties = Property.objects.all()
    return render(request, 'properties.html', {'properties': properties})


# Список проектів
def project_list(request):

    # Витягування з бд всх Проектів
    projects = Project.objects.order_by('pk').all()[::-1]

    len_projects = len(projects)

    # Пагінація
    paginator = Paginator(projects, 8)  # Вказуємо кількість елементів на сторінку
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    meta = Description.objects.get(template="Projects")
    return render(request, 'projects-list.html', locals())


# Проект детально (з Розробником + Обєктами + Районом + Питанями + Відгуками)
def project_detail(request, project_slug):

    # #################################################################################################-project
    # Витягування з бд Проект по ід
    project = Project.objects.get(project_slug=project_slug)

    # Витягування з бд Категорії Обєктів всі дані що стосуються проекту
    facilities_categories = project.facilities_category.all()

    # Обробка опису Розробника
    description_all = str(project.developer.description).replace("\r", "").split('\n')
    description_main = description_all[0]
    description_text = description_all[1:]

    # Обробка фото
    photos_list = []
    index = 1
    while True:
        photo_path = f"media/projects_photos/{project.photo_name}/photos/photo_id_1_{index}.jpg"
        # print(photo_path)
        if os.path.exists(photo_path):
            photos_list.append(photo_path)
            index += 1
        else:
            break

    # Витягування з бд Відгуки всі відгуки що стосуються проекту
    reviews = project.reviewsoverview_set.all()
    is_reviews = 1
    try:
        len_reviews = len(reviews)
        list_for_star = [1, 2, 3, 4, 5, 6, 7, 8]

        property_r = [i.property_r for i in reviews]
        agent_support = [i.agent_support for i in reviews]
        value_for_money = [i.value_for_money for i in reviews]
        location = [i.location for i in reviews]

        property_r = calculate_average(property_r)
        agent_support = calculate_average(agent_support)
        value_for_money = calculate_average(value_for_money)
        location = calculate_average(location)

        reviews_list = [[round(property_r * 20), property_r, 'Property'],
                        [round(agent_support * 20), agent_support, 'Agent Support'],
                        [round(value_for_money * 20), value_for_money, 'Value for Money'],
                        [round(value_for_money * 20), location, 'Location']]

        average_reviews = round(calculate_average([round(property_r), round(agent_support), round(value_for_money), round(location)]))
    except:
        is_reviews = 0
    # #################################################################################################-end project

    # #################################################################################################-Overview
    # Витягування з бд Району якому належать цей проект
    overview_detail = Overview.objects.get(project=project)

    # Витягування з бд Проектів які належать цьому району
    overview_projects = Project.objects.filter(overview_key=overview_detail)

    # Витягування з бд Oбєктів які належать цьому району
    properties_list = Property.objects.filter(project__in=overview_projects)

    sell_properties = [i for i in properties_list if "sell" in i.listing_type]
    rent_properties = [i for i in properties_list if "rent" in i.listing_type]

    len_sell_properties = len(sell_properties)
    len_rent_properties = len(rent_properties)
    # #################################################################################################-end Overview

    # Витягування з бд Питань по таблиці Проект
    questions = Question.objects.filter(for_table='Project')

    # Витягування з бд Обєктів які належать цьомо проекту
    condos = Property.objects.filter(project=project)
    condos_len = len(condos)

    # Витягування з бд Проекти три інші проекта
    excluded_projects = Project.objects.exclude(project_slug=project_slug).order_by('?')[:3]
    len_excluded_projects = len(excluded_projects)

    questions = Question.objects.filter(for_table='Overview')

    return render(request, 'projects-detail.html', locals())


# список з Розробником
def developers_list(request):

    # Витягування з бд Розробника
    developers = Developer.objects.order_by('pk').all()

    search = '0'
    if request.method == 'POST':
        data = request.POST.get('input_data')
        developers = developers.filter(developer_name__icontains=data)
        if len(developers) == 0:
            search = 'There are no results for this query. try again)'

    len_developers = len(developers)

    # Пагінація
    paginator = Paginator(developers, 10)  # Вказуємо кількість елементів на сторінку
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    meta = Description.objects.get(template="Developers")
    return render(request, 'developers-list.html', locals())


# Розробник детально
def developers_detail(request, developer_slug):

    # Витягування з бд Проект по ід
    developer = Developer.objects.get(developer_slug=developer_slug)

    # Обробка опису Розробника
    description_all = str(developer.description).replace("\r", "").split('\n')
    description_main = description_all[0]
    description_text = description_all[1:]

    # Витягування з бд Проекта по ід
    projects_off_plan = Project.objects.filter(completion_status='Complited', developer=developer.pk)
    len_projects_off_plan = len(projects_off_plan)

    # Витягування з бд Проект по ід
    projects_completion_date = Project.objects.filter(completion_status='Not done', developer=developer.pk)
    len_projects_completion_date = len(projects_completion_date)
    return render(request, 'developers-detail.html', locals())


# список з Обєктів
def condos_list(request):
    properties_list = Property.objects.order_by('pk').all()[::-1]
    len_properties_list = len(properties_list)

    projects = Project.objects.order_by('pk').all()[::-1]
    condos_list = []

    for project in projects:
        condos = Property.objects.filter(project=project)
        condos_len = len(condos)
        condos_list.append([project.project_name, condos_len, project.project_slug])

    if request.user.is_authenticated:
        lists = Lists.objects.get(user=request.user)

    try:
        not_user = notUser.objects.get(csrf=request.session.session_key)
        lists = None
    except notUser.DoesNotExist:
        not_user = None

    properties_list = save_change_price(request, lists, not_user, properties_list)

    paginator = Paginator(properties_list, 10)  # Вказуємо кількість елементів на сторінку
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    meta = Description.objects.get(template="Condos")


    return render(request, 'condos-list.html', locals())


# Обєкти детально
def condos_detail(request, property_slug):

    # Витягування з бд Обєкта по ід
    condo = Property.objects.get(property_slug=property_slug)

    # Витягування з бд Категорії Обєктів всі дані що стосуються проекту
    facilities_categories = condo.project.facilities_category.all()

    # Обробка опису Розробника
    description_all = str(condo.project.developer.description).replace("\r", "").split('\n')
    description_main = description_all[0]
    description_text = description_all[1:]

    # Обробка фото
    photos_list = []
    index = 1
    while True:
        photo_path = f"media/condos_photos/{condo.photo_name}/photos/photo_id_{index}.jpg"
        # print(photo_path)
        if os.path.exists(photo_path):
            photos_list.append(photo_path)
            index += 1
        else:
            break

    available_units = Property.objects.filter(project=condo.project.pk)
    available_units_len = len(available_units)

    questions = Question.objects.filter(for_table='Overview')

    reviews = condo.reviewsoverview_set.all()
    is_reviews = 1
    try:
        len_reviews = len(reviews)
        list_for_star = [1, 2, 3, 4, 5, 6, 7, 8]

        property_r = [i.property_r for i in reviews]
        agent_support = [i.agent_support for i in reviews]
        value_for_money = [i.value_for_money for i in reviews]
        location = [i.location for i in reviews]

        property_r = calculate_average(property_r)
        agent_support = calculate_average(agent_support)
        value_for_money = calculate_average(value_for_money)
        location = calculate_average(location)

        reviews_list = [[round(property_r * 20), property_r, 'Property'],
                        [round(agent_support * 20), agent_support, 'Agent Support'],
                        [round(value_for_money * 20), value_for_money, 'Value for Money'],
                        [round(value_for_money * 20), location, 'Location']]

        average_reviews = round(
            calculate_average([round(property_r), round(agent_support), round(value_for_money), round(location)]))
    except:
        is_reviews = 0

    # Витягування з бд Проекти три інші проекта
    excluded_projects = Project.objects.exclude(project_slug=condo.project.project_slug).order_by('?')[:3]
    len_excluded_projects = len(excluded_projects)

    return render(request, 'condos-detail.html', locals())


def about(request):
    about_first = About.objects.all()[0]
    about_description = str(about_first.description).split('\n')

    meta = Description.objects.get(template="About")
    return render(request, 'about.html', locals())


def blogs(request, settings=None):
    blogs = Blog.objects.order_by('-date').all()
    blogs_related = Blog.objects.order_by('-date')[:5]
    categories = Category.objects.all()
    tags = Tag.objects.all()

    if request.method == 'POST':
        data = request.POST.get('search')
        blogs_tags = blogs.filter(tag__name__icontains=data)

        blogs_categories = blogs.filter(category__name__icontains=data)


        blogs = list(set(blogs.filter(blog_name__icontains=data) | blogs_tags | blogs_categories))

        # if len(developers) == 0:
        #     search = 'There are no results for this query. try again)'

    if settings is not None:
        settings = str(settings).split(";")
        print(settings)
        if settings[0] == "category":
            category = Category.objects.get(category_slug=settings[1])
            blogs = blogs.filter(category=category)

        if settings[0] == "tags-cloud":
            tag = Tag.objects.get(tag_slug=settings[1])
            blogs = blogs.filter(tag=tag)
            print(blogs)
            print(tag)
            print(settings[1])

    len_blogs = len(blogs)

    paginator = Paginator(blogs, 12)  # Вказуємо кількість елементів на сторінку
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    meta = Description.objects.get(template="Blogs")
    return render(request, 'blog.html', locals())


def blog_detail(request, blog_slug):
    blog_detail = Blog.objects.get(blog_slug=blog_slug)
    blogs = Blog.objects.exclude(blog_slug=blog_slug).order_by('-date')[:5]
    categories = blog_detail.category.all()
    tags = blog_detail.tag.all()

    return render(request, 'blog-detail.html', locals())


def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Створення об'єкта моделі Contact і збереження його в базі даних
            contact = Contact(name=name, email=email, subject=subject, message=message)
            contact.save()

            # Після збереження об'єкта, можна перенаправити користувача на іншу сторінку
            return render(request, 'about.html')
    else:
        form = ContactForm()
    meta = Description.objects.get(template="Contacts")
    return render(request, 'contacts.html', locals())


def get_area_suggestions(request):
    input_text = request.GET.get('input', '')

    # Отримання всіх імен name_overview з моделі Overview
    overviews = Overview.objects.values_list('name_overview', flat=True)

    # Фільтрування підказок, які відповідають введеному тексту
    suggestions = [overview for overview in overviews if input_text.lower() in overview.lower()]

    return JsonResponse(suggestions, safe=False)


def get_project_suggestions(request):
    input_text = request.GET.get('input', '')
    projects = Project.objects.filter(project_name__icontains=input_text).values_list('project_name', flat=True)
    return JsonResponse(list(projects), safe=False)


def get_developer_suggestions(request):
    input_text = request.GET.get('input', '')
    developers = Developer.objects.filter(developer_name__icontains=input_text).values_list('developer_name', flat=True)
    return JsonResponse(list(developers), safe=False)


def get_property_suggestions(request):
    input_text = request.GET.get('input', '')
    properties = Property.objects.filter(property_name__icontains=input_text).values_list('property_name', flat=True)
    return JsonResponse(list(properties), safe=False)


def get_address_suggestions(request):
    input_text = request.GET.get('input', '')
    addresses = Property.objects.filter(address__icontains=input_text).values_list('address', flat=True)
    print(addresses)
    return JsonResponse(list(addresses), safe=False)


def index(request, settings=None):

    print(settings)
    developers = Developer.objects.all()
    condos = Property.objects.all()

    if request.user.is_authenticated:
        lists = Lists.objects.get(user=request.user)

    condos_all = condos
    war_message = ""
    average_latitude = 0
    average_longitude = 0

    if settings is not None:
        settings = str(settings)[1:].split(";")
        filters = {}

        for setting in settings:
            key, value = setting.split("=")
            filters[key] = value

        if "price-min" in filters:
            condos = condos.filter(sold_price__gte=filters["price-min"])
            price_min_value = filters["price-min"]
        if "price-max" in filters:
            condos = condos.filter(sold_price__lte=filters["price-max"])
            price_max_value = filters["price-max"]
        if "area" in filters:
            overview = Overview.objects.filter(name_overview=filters["area"]).first()
            condos = condos.filter(project__overview_key=overview)
            area_value = filters["area"]
        if "projects" in filters:
            project = Project.objects.filter(project_name=filters["projects"]).first()
            condos = condos.filter(project=project)
            project_value = filters["projects"]
        if "developers" in filters:
            developer = Developer.objects.filter(developer_name=filters["developers"]).first()
            condos = condos.filter(project__developer=developer)
            developers_value = filters["developers"]
        if "properties" in filters:
            condos = Property.objects.filter(property_name=filters["properties"])
            properties_value = Property.objects.filter(property_name=filters["properties"]).first()
        if "subarea" in filters:
            condos = condos.filter(address=filters["subarea"])
            subarea_value = filters["subarea"]
        if "ptypes" in filters:
            ptypes = {
                '1': "House",
                '2': "Villa",
                '3': "Condo",
                '4': "Apartment",
                '5': "Townhouse",
                '6': "Land",
                '7': "Shophouse",
            }
            condos = condos.filter(property_type=ptypes[filters["ptypes"]])
            ptypes_value = filters["ptypes"]
            ptypes_value_name = ptypes[filters["ptypes"]]
        if "bedrooms" in filters:
            bedrooms_filter = filters["bedrooms"].replace("+", "")
            condos = condos.filter(bedrooms__gte=bedrooms_filter)
            bedrooms_value = filters["bedrooms"]
        if "date" in filters:
            date_filter = filters["date"]
            if date_filter == "today":
                # Фільтрувати за сьогоднішньою датою
                condos = condos.filter(date=date.today())
            elif date_filter == "this week":
                # Фільтрувати за поточним тижнем
                start_date = date.today() - timedelta(days=date.today().weekday())
                end_date = start_date + timedelta(days=7)
                condos = condos.filter(date__range=(start_date, end_date))
            elif date_filter == "this month":
                # Фільтрувати за поточним місяцем
                start_date = date.today().replace(day=1)
                end_date = (start_date + timedelta(days=32)).replace(day=1) - timedelta(days=1)
                condos = condos.filter(date__range=(start_date, end_date))
            elif date_filter == "this year":
                # Фільтрувати за поточним роком
                start_date = date.today().replace(month=1, day=1)
                end_date = start_date.replace(month=12, day=31)
                condos = condos.filter(date__range=(start_date, end_date))
            elif date_filter == "all":
                pass
            else:
                war_message = 'There are no properties with these filters. Try again!'

        if ("radius" in filters and "area" in filters) or ("radius" in filters and "subarea" in filters):
            if len(condos) >= 1:
                average_latitude = [float(i.latitude) for i in condos]
                average_longitude = [float(i.longitude) for i in condos]
                print(average_latitude, average_longitude)
                average_latitude = round(sum(average_latitude) / len(average_latitude), 6)
                average_longitude = round(sum(average_longitude) / len(average_longitude), 7)
                # Викликаємо функцію find_condos_in_radius для знаходження квартир в радіусі
                condos = find_condos_in_radius(average_latitude, average_longitude, condos, condos_all, int(filters["radius"]))
            radius_value = filters["radius"]

        elif "radius" in filters and "pointOfInterest" in filters:
            grand_palace_coordinates = get_coordinates(filters["pointOfInterest"])
            if grand_palace_coordinates and len(condos) >= 1:
                latitude, longitude = grand_palace_coordinates
                print(f'Latitude: {latitude}, Longitude: {longitude}')
                condos = find_condos_in_radius(latitude, longitude, [], condos_all, int(filters["radius"]))
                point_interest_value = filters["pointOfInterest"]
                radius_value = filters["radius"]
            else:
                print('Не вдалося отримати координати')
            pass

        if "schools" in filters:
            if filters["schools"] != "All":
                condos = find_in_radius(condos, float(str(filters["schools"]).replace(" km", "")), schools)
            schools_value = filters["schools"]

        if "hospitals" in filters:
            if filters["hospitals"] != "All":
                condos = find_in_radius(condos, float(str(filters["hospitals"]).replace(" km", "")), hospitals)
            hospitals_value = filters["hospitals"]

    if len(condos) == 0:
        war_message = 'There are no properties with these filters. Try again!'
        condos = Property.objects.all()

    average_latitude = [float(i.latitude) for i in condos]
    average_longitude = [float(i.longitude) for i in condos]
    average_latitude = round(sum(average_latitude) / len(average_latitude), 6)
    average_longitude = round(sum(average_longitude) / len(average_longitude), 7)

    meta = Description.objects.get(template="Index")

    try:
        not_user = notUser.objects.get(csrf=request.session.session_key)
        lists = None
    except notUser.DoesNotExist:
        not_user = None

    condos = save_change_price(request, lists, not_user, condos)

    return render(request, 'index.html', locals())


def overviews(request):
    overview_detail = Overview.objects.order_by('pk')[0]

    overview_projects = Project.objects.filter(overview_key=overview_detail)

    properties = Property.objects.filter(project__in=overview_projects)

    sell_properties = [i for i in properties if "Sell" in i.listing_type]
    rent_properties = [i for i in properties if "Rent" in i.listing_type]

    len_sell_properties = len(sell_properties)
    len_rent_properties = len(rent_properties)

    print(len(overview_projects), "-----------------------0000")

    text = str(overview_detail.text).split("\n")

    questions = Question.objects.filter(for_table='Overview')

    overview_projects = Project.objects.filter(overview_key=overview_detail)
    overview_projects_len = len(overview_projects)

    reviews = overview_detail.reviewsoverview_set.all()
    is_reviews = 1
    try:
        len_reviews = len(reviews)
        list_for_star = [1, 2, 3, 4, 5, 6, 7, 8]

        property_r = [i.property_r for i in reviews]
        agent_support = [i.agent_support for i in reviews]
        value_for_money = [i.value_for_money for i in reviews]
        location = [i.location for i in reviews]

        property_r = calculate_average(property_r)
        agent_support = calculate_average(agent_support)
        value_for_money = calculate_average(value_for_money)
        location = calculate_average(location)

        reviews_list = [[round(property_r * 20), property_r, 'Property'],
                        [round(agent_support * 20), agent_support, 'Agent Support'],
                        [round(value_for_money * 20), value_for_money, 'Value for Money'],
                        [round(value_for_money * 20), location, 'Location']]

        average_reviews = round(
            calculate_average([round(property_r), round(agent_support), round(value_for_money), round(location)]))
    except:
        is_reviews = 0

    print(reviews)

    return render(request, 'overviews.html', locals())


def overviews_v2(request):
    return render(request, 'overviews-v2.html', locals())


def calculate_average(lst):
    if len(lst) == 0:
        return None
    new_lst = [i for i in lst if isinstance(i, int)]
    try:
        average = sum(new_lst) / len(new_lst)
    except ZeroDivisionError:
        average = '-'

    return average


# class LoginUserView(FormView):
#     form = ContactForm
#     template_name = 'contact.html'
#     success_url = reverse_lazy('about')
#
#     def form_valid(self, form):
#         name = form.cleaned_data['name']
#         email = form.cleaned_data['email']
#         subject = form.cleaned_data['subject']
#         message = form.cleaned_data['message']


@login_required
def add_to_wish_list(request, property_id):
    # Перевірити, чи існує користувач
    user = request.user
    if not user:
        return JsonResponse({'message': 'User not found.'}, status=400)

    # Опрацювати додавання до списку бажань
    try:
        wish_list = Lists.objects.get(user=user)
    except Lists.DoesNotExist:
        wish_list = Lists.objects.create(user=user)

    property_obj = Property.objects.get(id=property_id)

    # Перевірити, чи вже існує запис у списку бажань
    if property_obj in wish_list.wish_list.all():
        # Якщо так, видалити його
        wish_list.wish_list.remove(property_obj)
        message = 'Property removed from wish list.'
        is_added = False
    else:
        # Якщо немає, додати його
        wish_list.wish_list.add(property_obj)
        message = 'Property added to wish list.'
        is_added = True

    # Повернути відповідь у форматі JSON
    return JsonResponse({'message': message, 'is_added': is_added})


def wish_list(request):
    try:
        if request.method == 'POST':
            mail = request.POST.get('mail')  # Отримуємо значення поля "mail" з POST-запиту

            if not mail:  # Перевіряємо, чи поле "mail" пусте
                # Отримуємо об'єкт списку бажань для поточного користувача
                lists = Lists.objects.get(user=request.user)

                # Видаляємо всі об'єкти зі списку бажань
                lists.wish_list.clear()

                # Повертаємо користувача на сторінку списку бажань
                return redirect('wish-list')
            else:

                try:
                    validate_email(mail)  # Перевірка валідності електронної адреси
                except ValidationError:
                    message_error = 'Invalid email address!'
                    return render(request, 'wish-list.html', {'message_error': message_error})

                lists = Lists.objects.get(user=request.user)

                wish_list = lists.wish_list.all()
                message_mail = ''
                for prop in wish_list:
                    message_mail += f"\n http://127.0.0.1:8000/condo/{prop.property_slug}"

                subject = f'Wish list from {request.user.username}'
                message = f'User {request.user.username} shared his wish list with you:\n{message_mail}'
                from_email = 'bangkok.condos.for.sale.rent@gmail.com'
                recipient_list = [mail]

                send_mail(subject, message, from_email, recipient_list)

        lists = Lists.objects.get(user=request.user)
    except:
        print("Error")
    return render(request, 'wish-list.html', locals())


@login_required
def add_to_compare_list(request, property_id):
    user = request.user
    if not user:
        return JsonResponse({'message': 'User not found.'}, status=400)

    try:
        compare_list = Lists.objects.get(user=user)
    except Lists.DoesNotExist:
        compare_list = Lists.objects.create(user=user)

    property_obj = Property.objects.get(id=property_id)

    if property_obj in compare_list.compare_list.all():
        compare_list.compare_list.remove(property_obj)
        message = 'Property removed from compare list.'
        is_added = False
    else:
        compare_list.compare_list.add(property_obj)
        message = 'Property added to compare list.'
        is_added = True

    return JsonResponse({'message': message, 'is_added': is_added})


def compare_list(request, pk=0):
    if request.method == 'POST':

        lists = Lists.objects.get(user=request.user)

        if pk == 0:
            # Видалення всіх елементів зі списку порівняння
            lists.compare_list.clear()
        else:
            # Видалення конкретного елемента зі списку порівняння
            prop = get_object_or_404(Property, pk=pk)
            lists.compare_list.remove(prop)

        lists.save()

    try:
        lists = Lists.objects.get(user=request.user)
    except:
        pass
    return render(request, 'compare-list.html', locals())


def save_search(request, search):
    search = str(search)
    if request.method == 'POST':
        # Отримати поточного користувача (залежно від вашої автентифікаційної системи)
        user = request.user

        # Перевірити, чи існує запис для поточного користувача
        try:
            user_lists = Lists.objects.get(user=user)
            searches = user_lists.search
            if searches == None or searches == "":
                user_lists.search = search
            else:
                indeficator = False

                for i in str(searches).split("&&"):
                    if str(i) == search:
                        indeficator = True

                if indeficator == False:
                    user_lists.search = f"{searches}&&{search}"

            user_lists.save()

        except Lists.DoesNotExist:
            # Запису не існує, створити новий
            user_lists = Lists.objects.create(user=user, search=search)

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})


def manage_search(request):
    list_obj = Lists.objects.get(user=request.user)
    search_list = list_obj.search.split("&&")
    settings = [[setting[1:].split(";"), index] for index, setting in enumerate(search_list) if setting]

    if request.method == 'POST':
        index = request.POST.get('index')
        if index == None:
            settings = []
            list_obj.search = ''
            list_obj.save()
        else:
            index = int(index)
            del settings[index]
            print(settings)
            # Оновлення поля search об'єкта Lists в базі даних з оновленим списком settings
            sett = [';' + ';'.join(setting[0]) for setting in settings]
            list_obj.search = '&&'.join(sett)
            list_obj.save()

    return render(request, 'manage-search.html', {'settings': settings})


