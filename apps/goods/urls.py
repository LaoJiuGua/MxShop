from django.urls import path, include

from goods.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'goods', GoodsListViewSet, basename='goods')
router.register(r'categorys', CategoryViewSet, basename='categorys')
# 配置首页轮播图的url
router.register(r'banners', BannerViewset, basename="banners")
# 热搜词
router.register(r'hotsearchs', HotSearchsViewset, basename="hotsearchs")
# 首页系列商品展示url
router.register(r'indexgoods', IndexCategoryViewset, basename="indexgoods")

urlpatterns = [
   #商品列表页
    path('',include(router.urls))
]