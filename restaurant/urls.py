from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from restaurant.user.views import UserViewSet
from restaurant.menu.views import MenuViewSet, DishViewSet, CategoryViewSet, MenuSectionViewSet


# Routers
router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'menus', MenuViewSet)
router.register(r'dishes', DishViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'menu-sections', MenuSectionViewSet)

# Routes
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
