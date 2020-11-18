from django.db import models

class Dish(models.Model):
    name = models.CharField(max_length=255, blank=False)
    category = models.ForeignKey('menu.Category', on_delete=models.SET_NULL, null=True)
    section = models.ForeignKey('menu.MenuSection', on_delete=models.SET_NULL, null=True)
    price = models.FloatField(blank=False)
    description = models.TextField()
    active = models.BooleanField(default=True)


class Menu(models.Model):
    name = models.CharField(max_length=255, blank=False)
    active = models.BooleanField(default=True)
    dishes = models.ManyToManyField(Dish)


class Category(models.Model):
    name = models.CharField(max_length=255, blank=False)


class MenuSection(models.Model):
    name = models.CharField(max_length=255, blank=False)
