from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('creation/', views.creation, name='creation'),
    path('agent/parsing/', views.parsing, name='parsing'),
    path('agent/overviews/', views.agent_overviews, name='agent_overviews'),
    path('agent/projects/', views.agent_projects, name='agent_projects'),
    path('agent/properties/', views.agent_properties, name='agent_properties'),
    path('agent/properties/<str:items_per_page>/<str:sort_order>/', views.agent_properties, name='agent_properties_sort'),
    path('agent/property_create/', views.property_create, name='agent_property_create'),
    path('agent/property_update/<int:pk>/', views.PropertyUpdateView.as_view(), name='property_update'),

    path('property/<int:property_id>/', views.property_details, name='property_details'),
    path('properties/', views.properties, name='properties'),
    path('projects/', views.project_list, name='project_list'),
    path('project/<str:project_slug>/', views.project_detail, name='project_detail'),
    path('developers/', views.developers_list, name='developers_list'),
    path('developer/<str:developer_slug>/', views.developers_detail, name='developers_detail'),
    path('condos/', views.condos_list, name='condos_list'),
    path('condo/<str:property_slug>/', views.condos_detail, name='condos_detail'),
    path('about/', views.about, name='about'),
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/<str:settings>/', views.blogs, name='blogs'),
    path('blog/<str:blog_slug>/', views.blog_detail, name='blog_detail'),
    path('contacts/', views.contacts, name='contacts'),

    path('get_area_suggestions/', views.get_area_suggestions, name='get_area_suggestions'),
    path('get_project_suggestions/', views.get_project_suggestions, name='get_project_suggestions'),
    path('get_developer_suggestions/', views.get_developer_suggestions, name='get_developer_suggestions'),
    path('get_property_suggestions/', views.get_property_suggestions, name='get_property_suggestions'),
    path('get_address_suggestions/', views.get_address_suggestions, name='get_address_suggestions'),

    path('add-to-wish-list/<int:property_id>/', views.add_to_wish_list, name='add-to-wish-list'),
    path('add-to-compare-list/<int:property_id>/', views.add_to_compare_list, name='add-to-compare-list'),

    path('wish-list/', views.wish_list, name='wish-list'),
    path('compare-list/', views.compare_list, name='compare-list'),
    path('compare-list/<int:pk>/', views.compare_list, name='compare-list'),

    path('save-search/<str:search>', views.save_search, name='save_search'),
    path('manage-search/', views.manage_search, name='manage_search'),

    path('index/', views.index, name='index'),
    path('index/<str:settings>/', views.index, name='index'),
    path('overviews/', views.overviews, name='overviews'),
    path('overviews_v2/', views.overviews_v2, name='overviews_v2'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
