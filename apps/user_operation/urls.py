from django.urls import path, include

from user_operation.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'userfavs', UserFavViewset, basename='code')

urlpatterns = [
   #商品列表页
    path('',include(router.urls))
]