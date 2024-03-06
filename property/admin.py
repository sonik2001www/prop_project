from django.contrib import admin
from .models import *


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        'property_name',
        'pk',
        'external_property_id',
        'listing_type',
        'property_type',
        'project',
    )


@admin.register(Photo)
class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        'property',
        'image',
    )


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = (
        'developer_name',
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'overview_key',
        'developer',
        'project_name',
    )
    filter_horizontal = ('facilities_category',)
    search_fields = ['project_name']
    # autocomplete_fields = ['overview_key']
    # filter_horizontal = ('overview_key',)


@admin.register(FacilitiesCategory)
class FacilitiesCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')  # Поля, які будуть відображатися в списку
    list_filter = ('category',)  # Поля, за якими можна фільтрувати дані
    search_fields = ('name',)  # Поля, за якими можна здійснювати пошук


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('about_title', 'about_name', 'green_text', 'description', 'photo_name')  # Поля, які будуть відображатися в списку


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_name', 'blog_long_name', 'status', 'date', 'first_description', 'second_description', 'quote', 'author_quote', 'photo_name')  # Поля, які будуть відображатися в списку
    filter_horizontal = ('tag', 'category')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


@admin.register(Contact)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')


@admin.register(Overview)
class OverviewAdmin(admin.ModelAdmin):
    list_display = ('name_overview', 'buy_price_first', 'buy_price_second')



@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id_answer', 'for_table', 'question', 'answer')


@admin.register(ReviewsOverview)
class ReviewsOverviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')


@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    list_display = ('description', 'title')


@admin.register(Lists)
class ListsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user')
    filter_horizontal = ('wish_list', 'compare_list')


@admin.register(notUser)
class notUserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'csrf', 'currency_switcher')

