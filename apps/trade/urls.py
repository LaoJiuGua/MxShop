from django.urls import path, include

from trade.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# 购物车功能url配置
router.register(r'shopcarts', ShoppingCartViewset, basename='shopcarts')
# 订单url配置
router.register(r'orders', OrderViewset, basename="orders")

urlpatterns = [
   #商品列表页
    path('',include(router.urls))
]