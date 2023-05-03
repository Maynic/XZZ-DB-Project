from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import *
from .serializers import *

@api_view(['GET', 'POST'])
def visitor_list(request):
    if request.method == 'GET':
        print(request.method)
        data = xzz_visitor.objects.all()

        serializer = VisitorSerializer(data, context={'request': request}, many=True)
        # print(serializer.data)
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
        serializer = VisitorSerializer(object, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
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
        serializer = AttractionSerializer(object, data=request.data,context={'request': request})
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
        serializer = OrderSerializer(object, data=request.data,context={'request': request})
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
        serializer = ParkingSerializer(object, data=request.data,context={'request': request})
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
        serializer = PaymentSerializer(object, data=request.data,context={'request': request})
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
