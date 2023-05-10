from django.shortcuts import get_object_or_404
from django.core import serializers
from django.contrib.auth.hashers import make_password
from datetime import datetime
import json
from .models import *

#This function use email to find all the order that associate with this email address
def FindBookingDeails(id):
    user_login = get_object_or_404(xzz_user_login, id=id)
    email = user_login.email

    visitors = get_object_or_404(xzz_visitor, email=email)
    orders = xzz_order.objects.filter(xzz_visitor_id=visitors.pk)
    orders_ids = orders.values_list('pk', flat=True)

    tickets = xzz_ticket.objects.filter(visitor=visitors.pk)

    order_shows = xzz_orde_show.objects.filter(order_id__in=orders_ids)
    order_show_ids = order_shows.values_list('show_id', flat=True)
    shows = xzz_show.objects.filter(id__in=order_show_ids)
    # Create a dictionary to map show IDs to order IDs
    show_order_dict = {}
    for order_show in order_shows:
        show_id = order_show.show_id
        order_id = order_show.order_id
        if show_id not in show_order_dict:
            show_order_dict[show_id] = []
        show_order_dict[show_id].append(order_id)
    #print(show_order_dict)

    parks = xzz_parking.objects.filter(order_id__in=orders_ids)

    order_stores = xzz_orde_stor.objects.filter(order_id__in=orders_ids)
    # order_store_ids = order_stores.values_list('store_id', flat=True)
    # stores = xzz_store.objects.filter(id__in=order_store_ids)
    # order_dict = {}
    # for order_store in order_stores:
    #     store = stores.get(id=order_store.store_id)
    #     if store.id not in order_dict:
    #         order_dict[store.id] = []
    #     order_dict[store.id].append(order_store.id)

    data_ticket = json.loads(serializers.serialize('json', tickets))
    data_show = json.loads(serializers.serialize('json', shows))
    data_park = json.loads(serializers.serialize('json', parks))
    data_store = json.loads(serializers.serialize('json', order_stores))

    ticket_returned = []
    for obj in data_ticket:
        new_obj = {}
        fields = obj['fields']
        new_obj['ticket_method'] = fields['ticket_method']
        new_obj['visit_date'] = fields['visit_date']
        new_obj['ticket_price'] = fields['ticket_price']
        new_obj['order_number'] = fields['order']
        ticket_returned.append(new_obj)

    show_returned = []
    for obj in data_show:
        new_obj = {}
        fields = obj['fields']
        new_obj['show_name'] = fields['show_name']
        new_obj['show_description'] = fields['show_description']
        new_obj['show_type'] = fields['show_type']
        new_obj['start_time'] = fields['start_time']
        new_obj['end_time'] = fields['end_time']
        new_obj['show_price'] = fields['show_price']
        pk = obj['pk']
        new_obj['order_id'] = show_order_dict.get(pk)
        show_returned.append(new_obj)
    #print(show_returned)


    park_returned = []
    for obj in data_park:
        new_obj = {}
        fields = obj['fields']
        new_obj['lot'] = fields['lot']
        new_obj['spot'] = fields['spot']
        new_obj['time_in'] = fields['time_in']
        new_obj['time_out'] = fields['time_out']
        new_obj['fee'] = fields['fee']
        order_id = fields['order']
        order = xzz_order.objects.get(pk=order_id)
        new_obj['order_id'] = order.pk
        park_returned.append(new_obj)
    #print(park_returned)

    store_returned = []
    #print(data_store)
    for obj in data_store:
        new_obj = {}
        fields = obj['fields']
        # get corresponding order information under this order
        new_obj['menu_item_name'] = fields['menu_item_name']
        new_obj['menu_item_description'] = fields['menu_item_description']
        new_obj['menu_item_unit_price'] = fields['menu_item_unit_price']

        #now retrieve store information
        store_id = fields['store']
        store = xzz_store.objects.get(pk=store_id)

        new_obj['store_name'] = store.store_name
        new_obj['category'] = store.category
        store_returned.append(new_obj)

    #print(store_returned)
    return ticket_returned, show_returned, park_returned, store_returned

def PersonalInfo(id):
    user_visit = get_object_or_404(xzz_user_login, id=id)
    visitor_email = user_visit.email

    visitor = get_object_or_404(xzz_visitor, email=visitor_email)

    personalInfo = {}
    personalInfo['name'] = visitor.visitor_name
    personalInfo['email'] = visitor.email
    personalInfo['birth_date'] = visitor.birth_date
    personalInfo['phone'] = visitor.phone
    personalInfo['address'] = visitor.address
    personalInfo['city'] = visitor.city
    personalInfo['state'] = visitor.state
    personalInfo['zip'] = visitor.zip
    personalInfo['visitor_type'] = visitor.visitor_type
    personalInfo['password'] = make_password(user_visit.password)
    print(personalInfo)
    return personalInfo


####
####
#### helper functions to locate visitor email from user to database:
def get_visitor_id(userid):
    user = get_object_or_404(xzz_user_login, id=userid)
    visitor_email = user.email

    visitor = get_object_or_404(xzz_visitor, email=visitor_email)
    return visitor.id

