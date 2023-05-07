from django.shortcuts import get_object_or_404
from django.core import serializers
import json
from .models import *

#This function use email to find all the order that associate with this email address
def FindBookingDeails(id):
    user_login = get_object_or_404(xzz_user_login, id=id)
    email = user_login.email

    visitors = get_object_or_404(xzz_visitor, email=email)
    orders = xzz_order.objects.filter(xzz_visitor_id=visitors.pk)
    orders_ids = orders.values_list('pk', flat=True)

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

    order_store = xzz_orde_stor.objects.filter(order_id__in=orders_ids)
    order_store_ids = order_store.values_list('store_id', flat=True)
    stores = xzz_store.objects.filter(id__in=order_store_ids)

    data_show = json.loads(serializers.serialize('json', shows))
    data_park = json.loads(serializers.serialize('json', parks))
    data_store = json.loads(serializers.serialize('json', stores))

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
    for obj in data_store:
        new_obj = {}
        fields = obj['fields']
        new_obj['store_name'] = fields['store_name']
        new_obj['category'] = fields['category']
        order_id = fields.get('order', None)
        if order_id:
            order = xzz_order.objects.get(pk=order_id)
            new_obj['order_id'] = order.pk
        store_returned.append(new_obj)
    #print(store_returned)
    return show_returned, park_returned, store_returned

