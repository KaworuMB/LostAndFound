from django.urls import path
from .views import *
urlpatterns = [
    path('', item_list, name='item_list'),
    path('item/<int:item_id>/', item_detail, name='item_detail'),
    path('item/add/', item_create, name='item_create'),
    path('item/<int:item_id>/edit/', item_update, name='item_update'),
    path('item/<int:item_id>/delete/', item_delete, name='item_delete'),
]