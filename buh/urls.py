from django.urls import path
from . import views


app_name='buh'
urlpatterns = [
    path('', views.index_buh, name='index'),
    path('raznos/', views.raznos),
    path('settings/', views.settings),

    path('settings/address/create/', views.create_address, name='create_address'), #Addresses
    path('settings/address/', views.list_address, name='list_address'),
    path('settings/address/delete/', views.delete_address, name='delete_address'),
    path('settings/address/save/', views.save_address, name='save_address'),

    path('settings/customer/create/', views.create_customer, name='create_customer'), #Customers
    path('settings/customer/', views.list_customer, name='list_customer'),
    path('settings/customer/delete/', views.delete_customer, name='delete_customer'),
    path('settings/customer/save/', views.save_customer, name='save_customer'),

    path('naklad/new/', views.create_naklad, name='create_naklad'), # Naklad
    path('naklad/', views.list_naklad, name='list_naklad'),
    path('naklad/delete/', views.delete_naklad, name='delete_naklad'),
    path('naklad/save/', views.save_naklad, name='save_naklad'),

    path('pricelist/create/', views.create_pricelist, name='create_pricelist'), # PriceLists
    path('pricelist/', views.list_pricelist, name='list_pricelist'),
    path('pricelist/delete/', views.delete_pricelist, name='delete_pricelist'),
    path('pricelist/save/', views.save_pricelist, name='save_pricelist'),

    path('product/create/', views.create_product, name='create_product'), # Products
    path('product/', views.list_product, name='list_product'),
    path('product/delete/', views.delete_product, name='delete_product'),
    path('product/save/', views.save_product, name='save_product'),

    path('product/get_price/', views.get_price,
         name='get_price'),

]
