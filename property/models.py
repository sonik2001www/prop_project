from django.conf import settings
from django.db import models
from django import forms
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.mail import send_mail

from .aditional import find_condos_in_radius, get_coordinates, schools, hospitals, find_in_radius


class notUser(models.Model):
    csrf = models.CharField(max_length=200, null=True, blank=True)
    currency_switcher = models.CharField(max_length=10, null=True, blank=True, default='AED')


class Lists(models.Model):
    CHOICES_currency_switcher = {
        ('AED', 'AED'),
        ('US', 'US'),
        ('EUR', 'EUR'),
        ('JPY', 'JPY'),
        ('GBP', 'GBP'),
        ('AUD', 'AUD'),
        ('CAD', 'CAD'),
        ('CHF', 'CHF'),
        ('CNY', 'CNY'),
        ('HKD', 'HKD'),
        ('NZD', 'NZD'),
        ('SEK', 'SEK'),
        ('KRW', 'KRW'),
        ('SGD', 'SGD'),
        ('NOK', 'NOK'),
        ('MXN', 'MXN'),
        ('INR', 'INR'),
        ('BRL', 'BRL'),
        ('RUB', 'RUB'),
        ('ZAR', 'ZAR'),
        ('TRY', 'TRY'),
        ('PLN', 'PLN'),
        ('CZK', 'CZK'),
        ('THB', 'THB'),
        ('IDR', 'IDR'),
        ('HUF', 'HUF'),
        ('DKK', 'DKK'),
        ('ILS', 'ILS'),
        ('PHP', 'PHP'),
        ('MYR', 'MYR'),
    }
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    wish_list = models.ManyToManyField('property.Property', blank=True, related_name='users_wish_list')
    compare_list = models.ManyToManyField('property.Property', blank=True, related_name='users_compare_list')
    search = models.TextField(null=True, blank=True)
    currency_switcher = models.CharField(choices=CHOICES_currency_switcher, max_length=10, null=True, blank=True, default='AED')


class Description(models.Model):
    template = models.CharField(max_length=150, null=True, blank=True)
    title = models.CharField(max_length=150, null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True)

    class Meta:
        verbose_name = 'help Description'
        verbose_name_plural = 'help Descriptions'


class ReviewsOverview(models.Model):
    REVIEWS_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    overview = models.ForeignKey('property.Overview', on_delete=models.CASCADE, null=True, blank=True)
    project = models.ForeignKey('property.Project', on_delete=models.CASCADE, null=True, blank=True)
    property = models.ForeignKey('property.Property', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    surname = models.CharField(max_length=100, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    property_r = models.IntegerField(choices=REVIEWS_CHOICES, blank=True, null=True)
    agent_support = models.IntegerField(choices=REVIEWS_CHOICES, blank=True, null=True)
    value_for_money = models.IntegerField(choices=REVIEWS_CHOICES, blank=True, null=True)
    location = models.IntegerField(choices=REVIEWS_CHOICES, blank=True, null=True)
    average = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'help Review Overview'
        verbose_name_plural = 'help Reviews Overview'

    def save(self, *args, **kwargs):
        # Обчислюємо середнє значення
        fields_to_average = [
            'property_r',
            'agent_support',
            'value_for_money',
            'location'
        ]
        field_values = [getattr(self, field) for field in fields_to_average if getattr(self, field)]
        if field_values:
            average_value = round(sum(field_values) / len(field_values))
            self.average = average_value

        super().save(*args, **kwargs)


class Question(models.Model):
    CHOICES = (
        ('Overview', 'Overview'),
        ('Project', 'Project'),
    )
    id_answer = models.IntegerField()
    for_table = models.CharField(choices=CHOICES, max_length=100, null=True, blank=True)
    question = models.CharField(max_length=300, null=True, blank=True)
    answer = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'help Question'
        verbose_name_plural = 'help Questions'

    def review(self):
        return 1 if self.id_answer == 1 else 0


class Overview(models.Model):
    name_overview = models.CharField(max_length=100, null=True, blank=True)
    overview_slug = models.CharField(max_length=150, blank=True, null=True, unique=True)
    SEO_title = models.CharField(max_length=150, null=True, blank=True)
    SEO_description = models.CharField(max_length=300, null=True, blank=True)
    buy_price_first = models.DecimalField(max_digits=15, decimal_places=1, null=True, blank=True)
    buy_price_second = models.DecimalField(max_digits=15, decimal_places=1, null=True, blank=True)
    rent_price_first = models.DecimalField(max_digits=15, decimal_places=1, null=True, blank=True)
    rent_price_second = models.DecimalField(max_digits=15, decimal_places=1, null=True, blank=True)

    location = models.CharField(max_length=150, null=True, blank=True)
    distance_location = models.DecimalField(max_digits=15, decimal_places=1, null=True, blank=True)
    time_location = models.DecimalField(max_digits=15, decimal_places=1, null=True, blank=True)
    airport = models.CharField(max_length=150, null=True, blank=True)
    distance_airport = models.DecimalField(max_digits=15, decimal_places=1, null=True, blank=True)
    time_airport = models.DecimalField(max_digits=15, decimal_places=1, null=True, blank=True)

    text = models.TextField(null=True, blank=True)

    latitude = models.CharField(max_length=30, blank=True, null=True)
    longitude = models.CharField(max_length=30, blank=True, null=True)
    photo_name = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return self.name_overview

    class Meta:
        verbose_name = 'main Overview'
        verbose_name_plural = 'main Overviews'

    def save(self, *args, **kwargs):
        if self.name_overview:
            self.overview_slug = self.generate_overview_slug()
        super().save(*args, **kwargs)

    def generate_overview_slug(self):
        slug = slugify(self.name_overview)
        base_slug = slug
        index = 1
        index_all = ''
        while Overview.objects.filter(overview_slug=slug).exists():
            slug = f'{base_slug}{index_all}'
            index += 1
            index_all = f'-{index}'
        return slug


class Developer(models.Model):
    developer_name = models.CharField(max_length=150)
    developer_slug = models.CharField(max_length=150, blank=True, null=True, unique=True)
    SEO_title = models.CharField(max_length=150, null=True, blank=True)
    SEO_description = models.CharField(max_length=300, null=True, blank=True)
    project_count = models.IntegerField()
    total_no_of_units = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    developer_units = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    resale_units = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    video = models.URLField(blank=True, null=True)
    description = models.TextField()
    photo_name = models.CharField(max_length=40, blank=True, null=True)
    # project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.developer_name

    class Meta:
        verbose_name = 'main Developer'
        verbose_name_plural = 'main Developers'

    def save(self, *args, **kwargs):
        if self.developer_name:
            self.developer_slug = self.generate_developer_slug()
        super().save(*args, **kwargs)

    def generate_developer_slug(self):
        slug = slugify(self.developer_name)
        base_slug = slug
        index = 1
        index_all = ''
        while Developer.objects.filter(developer_slug=slug).exists():
            slug = f'{base_slug}{index_all}'
            index += 1
            index_all = f'-{index}'
        return slug


class Project(models.Model):
    PROPERTY_TYPE_CHOICES = (
        ('house', 'House'),
        ('villa', 'Villa'),
        ('condo', 'Condo'),
        ('apartment', 'Apartment'),
        ('townhouse', 'Townhouse'),
        ('land', 'Land'),
        ('shophouse', 'Shophouse'),
    )
    YOWERS_OR_BUILDINGS_FOR_CONDOS_CHOICES = (
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D'),
        ('e', 'E'),
        ('f', 'F'),
        ('g', 'G'),
    )
    SEVERAL_PHASES_FOR_HOUSE_CHOICES = (
        ('phase_1', 'Phase 1'),
        ('phase_2', 'Phase 2'),
        ('phase_3', 'Phase 3'),
        ('phase_4', 'Phase 4'),
        ('phase_5', 'Phase 5'),
    )
    PETS_ALLOWED_CHOICES = (
        ('yes_all_kinds', 'Yes all kinds'),
        ('cats_and_dogs_small_sized', 'Cats and Dogs (small sized)'),
        ('cats_and_dogs_any_sized', 'Cats and dogs (any size)'),
        ('only_cats', 'Only cats'),
        ('only_dogs', 'Only dogs'),
        ('no', 'No'),
    )
    FACILITIES_CHOICES = [
        ('concierge', 'Concierge'),
        ('golf_simulator', 'Golf Simulator'),
        ('gym', 'Gym'),
        ('security', '24h Security'),
        ('swimming_pool', 'Swimming Pool'),
        ('sauna', 'Sauna'),
        ('garden', 'Garden'),
        ('shop', 'Shop on Premise'),
        ('restaurant', 'Restaurant on Premise'),
        ('wifi', 'Wi-Fi'),
        ('playground', 'Playground / Kids area'),
        ('parking', 'Parking'),
        ('cctv', 'CCTV'),
        ('group_entertainment', 'Group Entertainment'),
        ('lounge', 'Lounge'),
        ('massage_room', 'Massage Room'),
        ('steam_room', 'Steam Room'),
        ('co_working_space', 'Co-working Space / Meeting Room'),
        ('library', 'Library / Reading Room'),
        ('key_card_access', 'Key Card Access'),
        ('reception', 'Reception / Lobby Area'),
        ('yoga_area', 'Yoga Area'),
        ('laundry', 'Laundry Facilities / Dry Cleaning'),
    ]

    COMPLETION_CHOICES = [
        ('Complited', 'Complited'),
        ('Not done', 'Not done'),
    ]

    status = models.BooleanField(default=True, blank=True, null=True)

    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=150)
    project_slug = models.CharField(max_length=150, blank=True, null=True, unique=True)
    SEO_title = models.CharField(max_length=150, null=True, blank=True)
    SEO_description = models.CharField(max_length=300, null=True, blank=True)

    units_num = models.IntegerField(blank=True, null=True)
    total_units = models.IntegerField(blank=True, null=True)

    overview_key = models.ForeignKey('property.Overview', on_delete=models.CASCADE, blank=True, null=True)

    starting_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    starting_price_rent = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    price_rent = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    underprised = models.CharField(max_length=10, blank=True, null=True)

    beach_name = models.CharField(max_length=100, blank=True, null=True)
    beach_distance = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    floors = models.IntegerField(blank=True, null=True)
    tower = models.IntegerField(blank=True, null=True)

    overview_o = models.TextField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    photo_name = models.CharField(max_length=40, blank=True, null=True)
    property_type = models.CharField(max_length=30, choices=PROPERTY_TYPE_CHOICES, blank=True, null=True)
    area = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)

    project_size = models.FloatField(blank=True, null=True)
    labd_size = models.FloatField(blank=True, null=True)

    monthly_rentals = models.IntegerField(blank=True, null=True)
    year_built = models.DateField(blank=True, null=True)
    completion_status = models.CharField(max_length=20, blank=True, null=True, choices=COMPLETION_CHOICES)

    off_plan = models.DateField(blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    towers_or_buildings_for_condos = models.CharField(max_length=30, choices=YOWERS_OR_BUILDINGS_FOR_CONDOS_CHOICES, blank=True, null=True)
    several_phases_for_house = models.CharField(max_length=30, choices=SEVERAL_PHASES_FOR_HOUSE_CHOICES, blank=True, null=True)

    pets_allowed = models.CharField(max_length=30, choices=PETS_ALLOWED_CHOICES, blank=True, null=True)
    video = models.URLField(blank=True, null=True)
    facilities_category = models.ManyToManyField('FacilitiesCategory', blank=True)

    management_information_fees = models.TextField(blank=True, null=True)
    map_latitude = models.FloatField(max_length=30, blank=True, null=True)
    map_longitude = models.FloatField(max_length=30, blank=True, null=True)

    average_price_for_sqm_in_building = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = 'main Project'
        verbose_name_plural = 'main Projects'

    def save(self, *args, **kwargs):
        if self.project_name:
            self.project_slug = self.generate_project_slug()
        super().save(*args, **kwargs)

    def generate_project_slug(self):
        slug = slugify(self.project_name)
        base_slug = slug
        index = 1
        index_all = ''
        while Project.objects.filter(project_slug=slug).exists():
            slug = f'{base_slug}{index_all}'
            index += 1
            index_all = f'-{index}'
        return slug


class FacilitiesCategory(models.Model):
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'help Facility Category'
        verbose_name_plural = 'help Facilities Category'


class Property(models.Model):
    INTERNAL_PROPERTY_ID_CHOICES = (
        ('Sell', 'Sell'),
        ('Rent', 'Rent'),
        ('Sell&Rent', 'Sell&Rent'),
    )
    BATHROOMS_CHOICES = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
    )
    BEDROOMS_CHOICES = (
        ('Studio', 'Studio'),
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
    )
    PROPERTY_TYPE_CHOICES = (
        ('House', 'House'),
        ('Villa', 'Villa'),
        ('Condo', 'Condo'),
        ('Apartment', 'Apartment'),
        ('Townhouse', 'Townhouse'),
        ('Land', 'Land'),
        ('Shophouse', 'Shophouse'),
    )
    FURNISHING_CHOICES = (
        ('Unfurnished', 'Unfurnished'),
        ('Fully Furnished', 'Fully Furnished'),
        ('Partly Furnished', 'Partly Furnished'),
        ('Bare Shell', 'Bare Shell'),
        ('Negotiable', 'Negotiable'),
    )
    OWNERSHIP_TYPE_CHOICES = (
        ('foreign_quota', 'Foreign Quota'),
        ('thai_quota', 'Thai Quota'),
        ('leasehold', 'Leasehold'),
        ('company', 'Company'),
    )
    LAND_OWNERSHIP_TYPE_CHOICES = (
        ('thai_ownership', 'Thai Ownership'),
        ('company', 'Company'),
        ('leasehold', 'Leasehold'),
    )
    LAND_TITLE_DEED_CHOICES = (
        ('chanote', 'Chanote'),
        ('sor_kor_1', 'Sor Kor 1'),
        ('nor_sor_2', 'Nor Sor 2'),
        ('nor_sor_3', 'Nor Sor 3'),
        ('nor_sor_3_gor', 'Nor Sor 3 Gor'),
    )
    UNIT_VIEW_CHOICES = (
        ('blocked_view', 'Blocked View'),
        ('360_views', '360° Views'),
        ('city_View', 'City View'),
        ('pool_view', 'Pool View'),
        ('park_view', 'Park View'),
        ('golf_course_view', 'Golf Course View'),
        ('unblocked_open_view', 'Unblocked Open View'),
        ('skyline_view', 'Skyline View'),
        ('river_canal_view', 'River or Canal View'),
        ('garden_view', 'Garden View'),
        ('lake_view', 'Lake View'),
    )

    # internal_property_id = models.CharField(max_length=30)
    # id = models.IntegerField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)

    date = models.DateField(blank=True, null=True)

    agent = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    status = models.BooleanField(default=True, blank=True, null=True)

    property_slug = models.CharField(max_length=150, blank=True, null=True, unique=True)
    SEO_title = models.CharField(max_length=150, null=True, blank=True)
    SEO_description = models.CharField(max_length=300, null=True, blank=True)

    # overview_key = models.ForeignKey('property.Overview', on_delete=models.CASCADE, blank=True, null=True)

    external_property_id = models.CharField(max_length=30, blank=True, null=True)
    listing_type = models.CharField(max_length=30, choices=INTERNAL_PROPERTY_ID_CHOICES, blank=True, null=True)
    property_type = models.CharField(max_length=30, choices=PROPERTY_TYPE_CHOICES, blank=True, null=True)
    property_name = models.CharField(max_length=150, blank=True, null=True)
    #
    # map_latitude = models.CharField(max_length=50, blank=True, null=True)
    # map_longitude = models.CharField(max_length=50, blank=True, null=True)

    area = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)

    bedrooms = models.CharField(choices=BEDROOMS_CHOICES, blank=True, null=True)
    bathrooms = models.CharField(choices=BATHROOMS_CHOICES, blank=True, null=True)
    buildings = models.IntegerField(blank=True, null=True)

    property_size = models.IntegerField(blank=True, null=True)
    outdoor_area_size = models.CharField(max_length=30, blank=True, null=True)
    land_size = models.CharField(max_length=30, blank=True, null=True)
    price_per_sqm_sold = models.FloatField(blank=True, null=True)
    price_per_sqm_rent = models.FloatField(blank=True, null=True)

    unit_number = models.CharField(max_length=30, blank=True, null=True)
    floor_number = models.IntegerField(blank=True, null=True)
    num_of_storeys = models.IntegerField(blank=True, null=True)
    furnishing = models.CharField(max_length=30, choices=FURNISHING_CHOICES, blank=True, null=True)
    num_of_parking_spaces = models.IntegerField(blank=True, null=True)
    monthly_maintenance_fee = models.IntegerField(blank=True, null=True)
    ownership_type = models.CharField(max_length=30, choices=OWNERSHIP_TYPE_CHOICES, blank=True, null=True)
    land_ownership_type = models.CharField(max_length=30, choices=LAND_OWNERSHIP_TYPE_CHOICES, blank=True, null=True)
    land_title_deed = models.CharField(max_length=30, choices=LAND_TITLE_DEED_CHOICES, blank=True, null=True)

    purchase_year_month = models.DateField(blank=True, null=True)
    construction_completed = models.DateField(blank=True, null=True)
    property_features = models.TextField(blank=True, null=True)
    property_outdoor_features = models.TextField(blank=True, null=True)
    unit_view = models.CharField(max_length=30, choices=UNIT_VIEW_CHOICES, blank=True, null=True)

    photo_name = models.CharField(max_length=50, blank=True, null=True)
    photo_links = models.TextField(blank=True, null=True)

    video = models.URLField(blank=True, null=True)
    virtual_tour = models.URLField(blank=True, null=True)
    floor_plan = models.URLField(blank=True, null=True)
    listing_title_for_sale = models.CharField(max_length=150, blank=True, null=True)
    listing_title_for_rent = models.CharField(max_length=150, blank=True, null=True)

    description = models.TextField(blank=True, null=True)
    for_sale_occupation_status = models.CharField(max_length=30, blank=True, null=True)
    for_sale_contract_expiry_date = models.DateField(blank=True, null=True)
    for_rent_occupation_status = models.CharField(max_length=30, blank=True, null=True)
    for_rent_available_date = models.DateField(blank=True, null=True)
    sales_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    rental_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    discounted_sales_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    discounted_rental_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    sold_price = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
    sold_date = models.DateField(blank=True, null=True)
    rent_price = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
    rent_date = models.DateField(blank=True, null=True)

    available_date = models.DateField(blank=True, null=True)
    hidden_private_info_form = models.TextField(blank=True, null=True)
    owner_name = models.CharField(max_length=150, blank=True, null=True)
    owner_phone_number = models.CharField(max_length=20, blank=True, null=True)
    owner_email = models.EmailField(blank=True, null=True)
    owner_social_accounts = models.TextField(blank=True, null=True)
    owner_info_display = models.CharField(max_length=30, blank=True, null=True)
    featured_property = models.BooleanField(default=False, blank=True, null=True)
    bold_property = models.BooleanField(default=False, blank=True, null=True)

    latitude = models.CharField(max_length=30, blank=True, null=True)
    longitude = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.property_name

    class Meta:
        verbose_name = 'main Condo'
        verbose_name_plural = 'main Condos'

    def basic_information(self):
        lst = []
        lst.append(["Property Type", self.property_type])
        lst.append(["Bedrooms", self.floor_number])
        lst.append(["Floor", self.property_size])
        lst.append(["Size", self.property_size])
        lst.append(["Price per SqM", self.price_sqm])
        lst.append(["Condo Ownership", self.ownership_type])
        lst.append(["Furniture", self.furnishing])
        lst.append(["View(s)", self.unit_view])
        lst.append(["CAM Fee", self.monthly_maintenance_fee])
        lst.append(["Unit ID", self.unit_number])
        return lst

    def outdoor_features(self):
        return str(self.property_outdoor_features).split('\r\n')

    def price_sqm(self):
        return str(float(self.price_per_sqm) * float(self.property_size))

    def get_property_features(self):
        return str(self.property_features).split(", ")

    def len_photos(self):
        return len(str(self.photo_links).split(",,"))

    def list_photos_3(self):
        list_photos = str(self.photo_links).split(",,")
        if len(list_photos) >= 3:
            list_photos = [list_photos[0], list_photos[1], list_photos[2]]
        elif len(list_photos) == 2:
            list_photos = [list_photos[0], list_photos[1], list_photos[0]]
        elif len(list_photos) == 1:
            list_photos = [list_photos[0], list_photos[0], list_photos[0]]
        else:
            list_photos = []

        print(list_photos, '---------')
        return list_photos

    def list_photos(self):
        return str(self.photo_links).split(",,")

    def get_photo_name(self):
        return '/media/condos_photos/' + str(self.photo_name) + '/photos/photo_id_1.jpg'

    def save(self, *args, **kwargs):
        # Отримати попередні значення sold_price та rent_price з бази даних
        previous_sold_price = Property.objects.filter(pk=self.pk).values_list('sold_price', flat=True).first()
        previous_rent_price = Property.objects.filter(pk=self.pk).values_list('rent_price', flat=True).first()

        if self.property_name:
            self.property_slug = self.generate_property_slug()

        if self.sold_price is not None:
            self.price_per_sqm_sold = round(self.sold_price / self.property_size, 2) if self.property_size else None
        if self.rent_price is not None:
            self.price_per_sqm_rent = round(self.rent_price / self.property_size, 2) if self.property_size else None

        # Перевірка на зміни в полях sold_price і rent_price
        updating_fields = kwargs.get('update_fields', None)
        if updating_fields is None or 'sold_price' not in updating_fields or 'rent_price' not in updating_fields:
            super().save(*args, **kwargs)  # Збереження моделі
            send_email(self.property_slug)  # Виклик функції після збереження

        if self.sold_price < previous_sold_price or self.rent_price < previous_rent_price:
            self.price_per_sqm_sold = round(self.sold_price / self.property_size, 2) if self.property_size else None
            self.price_per_sqm_rent = round(self.rent_price / self.property_size, 2) if self.property_size else None
            super().save(*args, **kwargs)  # Зберегти модель ще раз, щоб оновити price_per_sqm_sold та price_per_sqm_rent
            sent_email_for_price(self.property_slug)

    def generate_property_slug(self):
        slug = slugify(self.property_name)
        base_slug = slug
        index = 1
        index_all = ''
        while Property.objects.filter(property_slug=slug).exists():
            slug = f'{base_slug}{index_all}'
            index += 1
            index_all = f'-{index}'
        return slug


# @receiver(pre_save, sender=Property)
# def fill_coordinates(sender, instance, **kwargs):
#     if instance.project:
#         instance.latitude = instance.project.map_latitude
#         instance.longitude = instance.project.map_longitude


class Photo(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property_photos')
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return str(self.id)


class About(models.Model):
    about_title = models.CharField(max_length=150, null=True)
    about_name = models.CharField(max_length=150, null=True)
    green_text = models.CharField(max_length=250, null=True)
    description = models.TextField(null=True)
    photo_name = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return self.about_name

    class Meta:
        verbose_name = 'main About'
        verbose_name_plural = 'main About'


class Blog(models.Model):
    STATUS_CHOICES = (
        ('Hot', 'Hot'),
        ('New', 'New'),
    )
    blog_name = models.CharField(max_length=150, blank=True, null=True)
    blog_slug = models.CharField(max_length=150, blank=True, null=True, unique=True)
    SEO_title = models.CharField(max_length=150, null=True, blank=True)
    SEO_description = models.CharField(max_length=300, null=True, blank=True)
    blog_long_name = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    first_description = models.TextField(null=True, blank=True)
    second_description = models.TextField(null=True, blank=True)
    quote = models.TextField(null=True, blank=True)
    author_quote = models.CharField(max_length=50, null=True, blank=True)
    photo_name = models.CharField(max_length=50, null=True, blank=True)
    tag = models.ManyToManyField('Tag', blank=True)
    category = models.ManyToManyField('Category', blank=True)

    def __str__(self):
        return self.blog_name

    class Meta:
        verbose_name = 'main Blog'
        verbose_name_plural = 'main Blogs'

    def date2(self):
        date_all = str(self.date).split("-")
        return date_all[1] + ' ' + date_all[0]

    def day(self):
        date_all = str(self.date).split("-")
        return date_all[2]

    def save(self, *args, **kwargs):
        if self.blog_name:
            self.blog_slug = self.generate_blog_slug()
        super().save(*args, **kwargs)

    def generate_blog_slug(self):
        slug = slugify(self.blog_name)
        base_slug = slug
        index = 1
        index_all = ''
        while Blog.objects.filter(blog_slug=slug).exists():
            slug = f'{base_slug}{index_all}'
            index += 1
            index_all = f'-{index}'
        return slug


class Tag(models.Model):
    name = models.CharField(max_length=150)
    tag_slug = models.CharField(max_length=150, blank=True, null=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'other Tag'
        verbose_name_plural = 'other Tags'

    def save(self, *args, **kwargs):
        if self.name:
            self.tag_slug = self.generate_tag_slug()
        super().save(*args, **kwargs)

    def generate_tag_slug(self):
        slug = slugify(self.name)
        base_slug = slug
        index = 1
        index_all = ''
        while Tag.objects.filter(tag_slug=slug).exists():
            slug = f'{base_slug}{index_all}'
            index += 1
            index_all = f'-{index}'
        return slug


class Category(models.Model):
    name = models.CharField(max_length=150)
    category_slug = models.CharField(max_length=150, blank=True, null=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'other Category'
        verbose_name_plural = 'other Categories'

    def save(self, *args, **kwargs):
        if self.name:
            self.category_slug = self.generate_category_slug()
        super().save(*args, **kwargs)

    def generate_category_slug(self):
        slug = slugify(self.name)
        base_slug = slug
        index = 1
        index_all = ''
        while Category.objects.filter(category_slug=slug).exists():
            slug = f'{base_slug}{index_all}'
            index += 1
            index_all = f'-{index}'
        return slug


class Contact(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'main Contact'
        verbose_name_plural = 'main Contacts'


def send_email(slug):
    users = User.objects.all()

    for user in users:
        try:
            list = Lists.objects.get(user=user.pk)
            searches = str(list.search)

            if searches != None or searches != "":

                searches_list = searches.split("&&")
                for s in searches_list:

                    condos = Property.objects.filter(property_slug=slug)

                    settings = str(s)[1:].split(";")
                    filters = {}

                    for setting in settings:
                        key, value = setting.split("=")
                        filters[key] = value
                    if "price-min" in filters:
                        condos = condos.filter(sold_price__gte=filters["price-min"])
                    if "price-max" in filters:
                        condos = condos.filter(sold_price__lte=filters["price-max"])
                    if "area" in filters and not("radius" in filters):
                        overview = Overview.objects.filter(name_overview=filters["area"]).first()
                        condos = condos.filter(project__overview_key=overview)
                    if "projects" in filters:
                        project = Project.objects.filter(project_name=filters["projects"]).first()
                        condos = condos.filter(project=project)
                    if "developers" in filters:
                        developer = Developer.objects.filter(developer_name=filters["developers"]).first()
                        condos = condos.filter(project__developer=developer)
                    if "properties" in filters:
                        condos = Property.objects.filter(property_name=filters["properties"])
                    if "subarea" in filters and not("radius" in filters):
                        condos = condos.filter(address=filters["subarea"])
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
                    if "bedrooms" in filters:
                        bedrooms_filter = filters["bedrooms"].replace("+", "")
                        condos = condos.filter(bedrooms__gte=bedrooms_filter)
                    if ("radius" in filters and "area" in filters) or ("radius" in filters and "subarea" in filters):
                        average_latitude = [float(i.latitude) for i in condos]
                        average_longitude = [float(i.longitude) for i in condos]
                        average_latitude = round(sum(average_latitude) / len(average_latitude), 6)
                        average_longitude = round(sum(average_longitude) / len(average_longitude), 7)
                        # Викликаємо функцію find_condos_in_radius для знаходження квартир в радіусі
                        condos = find_condos_in_radius(average_latitude, average_longitude, condos, condos, int(filters["radius"]))

                    elif "radius" in filters and "pointOfInterest" in filters:
                        grand_palace_coordinates = get_coordinates(filters["pointOfInterest"])
                        if grand_palace_coordinates:
                            latitude, longitude = grand_palace_coordinates
                            print(f'Latitude: {latitude}, Longitude: {longitude}')
                            condos = find_condos_in_radius(latitude, longitude, [], condos, int(filters["radius"]))
                        else:
                            print('Не вдалося отримати координати')
                        pass
                    if "schools" in filters:
                        if filters["schools"] != "All":
                            condos = find_in_radius(condos, float(str(filters["schools"]).replace(" km", "")), schools)

                    if "hospitals" in filters:
                        if filters["hospitals"] != "All":
                            condos = find_in_radius(condos, float(str(filters["hospitals"]).replace(" km", "")), hospitals)

                    if len(condos) == 1:

                        subject = 'A new Property appeared'
                        message = f'can be viewed at the link: http://185.187.169.247/condo/{slug}'
                        from_email = 'bangkok.condos.for.sale.rent@gmail.com'
                        recipient_list = [user.email]

                        send_mail(subject, message, from_email, recipient_list)
        except:
            print("no element")


def sent_email_for_price(slug):
    users = User.objects.all()

    for user in users:
        try:
            list = Lists.objects.get(user=user.pk)
            wish_list = list.wish_list.all()
            for property in wish_list:
                condo = Property.objects.get(property_slug=slug)

                if property.pk == condo.pk:
                    subject = 'New price for the Property'
                    message = f'Can be viewed at the link: http://185.187.169.247/condo/{slug}'
                    from_email = 'bangkok.condos.for.sale.rent@gmail.com'
                    recipient_list = [user.email]

                    send_mail(subject, message, from_email, recipient_list)
        except:
            pass


