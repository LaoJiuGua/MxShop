from django.urls import path, include

from users.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'code', SmsCodeViewSet, basename='code')
router.register(r'', UserViewset, basename='users')


urlpatterns = [
   #商品列表页
    path('',include(router.urls))
]