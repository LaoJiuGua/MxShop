from django.urls import path, include

from goods.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'goods', GoodsListViewSet, basename='goods')
router.register(r'categorys', CategoryViewSet, basename='categorys')

urlpatterns = [
   #商品列表页
    path('',include(router.urls))
]