from rest_framework import serializers

from .models import Menu, Dish, Category, MenuSection


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['pk', 'name', 'dishes']


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['pk', 'name', 'dishes']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['pk', 'name', 'dishes']


class MenuSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['pk', 'name', 'dishes']
