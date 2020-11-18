from django.shortcuts import render
from rest_framework import viewsets

from .models import Menu, Dish, Category, MenuSection
from .serializers import MenuSerializer, DishSerializer, CategorySerializer, MenuSectionSerializer


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MenuSectionViewSet(viewsets.ModelViewSet):
    queryset = MenuSection.objects.all()
    serializer_class = MenuSectionSerializer
