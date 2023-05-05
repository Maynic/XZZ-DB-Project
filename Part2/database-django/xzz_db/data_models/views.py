from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from .models import *
from .serializers import *

@api_view(['GET', 'POST'])
def visitor_list(request):
    if request.method == 'GET':
        data = xzz_visitor.objects.all()

        serializer = VisitorSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VisitorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def visitor_detail(request, pk):
    try:
        visitor = xzz_visitor.objects.get(pk=pk)
    except xzz_visitor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = VisitorSerializer(visitor, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        visitor.delete()
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
def ticket_search(request):
    if request.method == 'POST':
        serializer = SearchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        data = xzz_ticket_search.objects.all()

        serializer = SearchSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

#enforce login
@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        print("GGGGG: ", request.POST)
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            print("Auth Success")
            login(request, user)
            return JsonResponse({'Login': True})
        print("Auth failed")
    return JsonResponse({'Login': False})

@csrf_exempt
def user_register(request):
    if request.method == 'POST':
        name = request.POST['ns_name']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username=email, password=password, first_name=name)
        user.save()
        return JsonResponse({'Register': True})

    return JsonResponse({'Register': False})
