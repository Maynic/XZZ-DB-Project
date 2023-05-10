"""
URL configuration for xzz_db project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from data_models import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/data_models/booking_details/<int:userid>', views.BookingDetails),
    path('api/data_models/setting_details/<int:userid>', views.SettingDetails),
    path('api/data_models/retrieve/', views.retrieve_visitor_id),

    path('api/data_models/user_login/', views.user_login),
    path('api/data_models/user/', views.user_list),
    path('api/data_models/update/<int:userid>', views.user_visitor_update),
    path('api/data_models/user_logout/', views.user_logout),
    path('api/data_models/get_show_name/', views.show_name),

    path('api/data_models/visitor/', views.visitor_list, name='visitor_list'),
    path('api/data_models/visitor/<int:pk>', views.visitor_detail, name='visitor_detail'),

    path('api/data_models/attraction/', views.attraction_list, name='attraction_list'),
    path('api/data_models/attraction/<int:pk>', views.attraction_detail, name='attraction_detail'),

    path('api/data_models/order/', views.order_list, name='order_list'),
    path('api/data_models/order/<int:pk>', views.order_detail, name='order_detail'),

    path('api/data_models/parking/', views.parking_list, name='parking_list'),
    path('api/data_models/parking/<int:pk>', views.parking_detail, name='parking_detail'),

    path('api/data_models/payment/', views.payment_list, name='payment_list'),
    path('api/data_models/payment/<int:pk>', views.payment_detail, name='payment_detail'),

    path('api/data_models/show/', views.show_list, name='show_list'),
    path('api/data_models/show/<int:pk>', views.show_detail, name='show_detail'),

    path('api/data_models/store/', views.store_list, name='store_list'),
    path('api/data_models/store/<int:pk>', views.store_detail, name='store_detail'),

    path('api/data_models/ticket/', views.ticket_list, name='ticket_list'),
    path('api/data_models/ticket/<int:pk>', views.ticket_detail, name='ticket_detail'),

    path('api/data_models/attraction_visit/', views.attraction_visit_list, name='attraction_visit_list'),
    path('api/data_models/attraction_visit/<int:pk>', views.attraction_visit_detail, name='attraction_visit_detail'),

    path('api/data_models/show_order/', views.show_order_list, name='show_order_list'),
    path('api/data_models/show_order/<int:pk>', views.show_order_detail, name='show_order_detail'),

    path('api/data_models/store_order/', views.store_order_list, name='store_order_list'),
    path('api/data_models/store_order/<int:pk>', views.store_order_detail, name='store_order_detail'),
    ]