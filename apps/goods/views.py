from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins, viewsets, filters
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from . import serializers
from .serializers import GoodsSerializer, CategorySerializer
from .models import Goods, GoodsCategory, GoodsImage
from .filter import GoodsFilter

from django_filters.rest_framework import DjangoFilterBackend


class GoodsPagination(PageNumberPagination):
    '''
    商品列表自定义分页
    '''
    #默认每页显示的个数
    page_size = 12
    #可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    #页码参数
    page_query_param = 'page'
    #最多能显示多少页
    max_page_size = 100


class CategoryViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    list:
        商品分类列表数据
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer

class GoodsListViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
        商品列表
    """
    # 这里必须要定义一个默认的排序,否则会报错
    queryset = Goods.objects.all().order_by('id')
    # 分页
    pagination_class = GoodsPagination
    serializer_class = GoodsSerializer
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)

    # 设置filter的类为我们自定义的类
    # 过滤
    filter_class = GoodsFilter
    # 搜索,=name表示精确搜索，也可以使用各种正则表达式
    search_fields = ('name','goods_brief','goods_desc')
    # 排序
    ordering_fields = ('sold_num','shop_price')


    # def get(self,request,*args,**kwargs):
    #     return self.list(request,*args,**kwargs)
    # def get(self, request, format=None):
    #     goods = Goods.objects.all()
    #     goods_serializer = GoodsSerializer(goods,many=True)
    #     return Response(goods_serializer.data)

