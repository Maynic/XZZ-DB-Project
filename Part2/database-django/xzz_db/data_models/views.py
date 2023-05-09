from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import JsonResponse
from django.http import QueryDict
from django.views.decorators.csrf import csrf_exempt
from .auth import MyAuthBackend
import json
from .Helper import *

from .models import *
from .serializers import *


@api_view(['GET', 'POST'])
def visitor_list(request):
    print(request.method)
    if request.method == 'GET':
        print(request.method)
        data = xzz_visitor.objects.all()
        serializer = VisitorSerializer(data, context={'request': request}, many=True)
        print(serializer.data)
        return Response(serializer.data)

    elif request.method == 'POST':
        if request.content_type == 'application/json':
            print("JSON data: ", request.body)
        serializer = VisitorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        print(serializer.errors)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def visitor_detail(request, pk):
    try:
        object = xzz_visitor.objects.get(pk=pk)
    except xzz_visitor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = VisitorSerializer(object, data=request.data, context={'request': request})
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


""" Search bar functions -zn
For ticket search, front end send GET with date, people to back-end. back end return calculated price.
For shows search, front end send GET with show name, show time (M/D/Y) and # of people. Backend return the corresponding info
For Store search, front end send GET with category, back end response with menus.
For Parking search, front end  send GET with category, back end response with calculated price.


For ticket and parking, front end will directly switch to check out page.
While shows and store will switch to a display information page.
POST request will be made after checked out by customer

"""


@api_view(['GET', 'POST'])
def SearchBar(request):
    if request.method == 'POST':
        print("JSON form: ", request.data)
        # deal with data
        # form1 is attraction
        price = ComputedPrice(request.data['form'], request.data)
        #print(price)
        return JsonResponse(price, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)


# API for obtain user orders information
# Or update user orders information
@api_view(['GET', 'POST'])
def BookingDetails(request, userid):
    ticket, show, park, store = FindBookingDeails(userid)
    data = {
        'ticket': ticket,
        'show': show,
        'park': park,
        'store': store
    }
    #print(data)
    return JsonResponse(data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def SettingDetails(request, userid):
    if request.method == 'GET':  # get user information
        personalinfo = PersonalInfo(userid)
        return JsonResponse(personalinfo, status=status.HTTP_200_OK)
    elif request.method == 'POST':  # update user information
        return Response(status=status.HTTP_200_OK)


# enforce login
# Current suport POST only
@api_view(['POST', 'GET'])
def user_login(request):
    # POST used to log in

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = MyAuthBackend.authenticate(request, email=email, password=password)

        if user is not None:
            if user:
                print("Auth Success")
                # request.session['user_id'] = user.id
                # request.session.modified = True

                return Response({"user_id": user.id}, status=status.HTTP_200_OK)
            else:
                # password not right
                return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


# @api_view(['POST'])
# def user_register(request):
#     if request.method == 'POST':
#         return redirect('visitor_list', permanent=False)
#
#     return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def user_logout(request):
    try:
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        data = xzz_user_login.objects.all()

        serializer = UserSerializer(data, context={'request': request}, many=True)
        print(serializer.data)
        return Response(serializer.data)

    elif request.method == 'POST':
        if request.content_type == 'application/json':
            print("JSON data: ", request.body)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        print(serializer.errors)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# safely retrieve visitor id from user_id
# This function return the corresponding visitor id based on userid
@api_view(['PUT'])
def user_visitor_update(request, userid):
    if request.method == 'PUT':
        visitor_id = get_visitor_id(userid)

        try:
            return redirect('visitor_detail', pk=visitor_id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def attraction_list(request):
    if request.method == 'GET':
        print(request.method)
        data = xzz_attraction.objects.all()

        serializer = AttractionSerializer(data, context={'request': request}, many=True)
        # print(serializer.data)
        return Response(serializer.data)

    elif request.method == 'POST':
        if request.content_type == 'application/json':
            print("JSON data: ", request.body)
        serializer = AttractionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        print(serializer.errors)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def attraction_detail(request, pk):
    try:
        object = xzz_attraction.objects.get(pk=pk)
    except xzz_attraction.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = AttractionSerializer(object, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def order_list(request):
    if request.method == 'GET':
        print(request.method)
        data = xzz_order.objects.all()

        serializer = OrderSerializer(data, context={'request': request}, many=True)
        # print(serializer.data)
        return Response(serializer.data)

    elif request.method == 'POST':
        if request.content_type == 'application/json':
            print("JSON data: ", request.body)
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        print(serializer.errors)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def order_detail(request, pk):
    try:
        object = xzz_order.objects.get(pk=pk)
    except xzz_order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = OrderSerializer(object, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def parking_list(request):
    if request.method == 'GET':
        print(request.method)
        data = xzz_parking.objects.all()

        serializer = ParkingSerializer(data, context={'request': request}, many=True)
        # print(serializer.data)
        return Response(serializer.data)

    elif request.method == 'POST':
        if request.content_type == 'application/json':
            print("JSON data: ", request.body)
        serializer = ParkingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        print(serializer.errors)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def parking_detail(request, pk):
    try:
        object = xzz_parking.objects.get(pk=pk)
    except xzz_parking.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ParkingSerializer(object, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def payment_list(request):
    if request.method == 'GET':
        print(request.method)
        data = xzz_payment.objects.all()

        serializer = PaymentSerializer(data, context={'request': request}, many=True)
        # print(serializer.data)
        return Response(serializer.data)

    elif request.method == 'POST':
        if request.content_type == 'application/json':
            print("JSON data: ", request.body)
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        print(serializer.errors)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def payment_detail(request, pk):
    try:
        object = xzz_payment.objects.get(pk=pk)
    except xzz_payment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PaymentSerializer(object, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# For ShowSerializer
@api_view(['GET', 'POST'])
def show_list(request):
    if request.method == 'GET':
        data = xzz_show.objects.all()
        serializer = ShowSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ShowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def show_detail(request, pk):
    try:
        object = xzz_show.objects.get(pk=pk)
    except xzz_show.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ShowSerializer(object, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# For StoreSerializer
@api_view(['GET', 'POST'])
def store_list(request):
    if request.method == 'GET':
        data = xzz_store.objects.all()
        serializer = StoreSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def store_detail(request, pk):
    try:
        object = xzz_store.objects.get(pk=pk)
    except xzz_store.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = StoreSerializer(object, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# For TicketSerializer
@api_view(['GET', 'POST'])
def ticket_list(request):
    if request.method == 'GET':
        data = xzz_ticket.objects.all()
        serializer = TicketSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def ticket_detail(request, pk):
    try:
        object = xzz_ticket.objects.get(pk=pk)
    except xzz_ticket.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = TicketSerializer(object, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# For AttractionVisitSerializer
@api_view(['GET', 'POST'])
def attraction_visit_list(request):
    if request.method == 'GET':
        data = xzz_attr_visi.objects.all()
        serializer = AttractionVisitSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AttractionVisitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def attraction_visit_detail(request, pk):
    try:
        object = xzz_attr_visi.objects.get(pk=pk)
    except xzz_attr_visi.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = AttractionVisitSerializer(object, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# For ShowOrderSerializer
@api_view(['GET', 'POST'])
def show_order_list(request):
    if request.method == 'GET':
        data = xzz_orde_show.objects.all()
        serializer = ShowOrderSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ShowOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def show_order_detail(request, pk):
    try:
        object = xzz_orde_show.objects.get(pk=pk)
    except xzz_orde_show.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ShowOrderSerializer(object, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# For StoreOrderSerializer
@api_view(['GET', 'POST'])
def store_order_list(request):
    if request.method == 'GET':
        data = xzz_orde_stor.objects.all()
        serializer = StoreOrderSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StoreOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def store_order_detail(request, pk):
    try:
        object = xzz_orde_stor.objects.get(pk=pk)
    except xzz_orde_stor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = StoreOrderSerializer(object, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
