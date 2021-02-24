from django.urls import path, include

from user_operation.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# 收藏功能url配置
router.register(r'userfavs', UserFavViewset, basename='code')
# 留言功能url配置
router.register(r'messages', LeavingMessageViewset, basename="messages")
# 收获地址url配置
router.register(r'address',AddressViewset, basename="address")

urlpatterns = [
   #商品列表页
    path('',include(router.urls))
]