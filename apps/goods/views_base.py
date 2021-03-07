from django.views.generic import View
from goods.models import Goods
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.versioning import HostNameVersioning
from rest_framework.permissions import BasePermission
from rest_framework.serializers import BaseSerializer
from rest_framework.serializers import Serializer
import jwt
import you_get


from celery import Celery

app = Celery('hello', broker='redis://localhost')

@app.task
def hello():
    return 'hello world'

# class A(APIView):
#     def get(self,request):
#         self.dispatch()
#
#         pass
#
# class GoodsListView(View):
#     def get(self,request):
#         # 通过django的view实现商品列表页
#         json_list = []
#         # 获取所有商品
#         goods = Goods.objects.all()
#         # for good in goods:
#         #     json_dict = {}
#         #     # 获取商品的每个字段，键值对形式
#         #     json_dict['name'] = good.name
#         #     json_dict['category'] = good.category.name
#         #     json_dict['market_price'] = good.market_price
#         #     json_list.append(json_dict)
#
#         # from django.forms.models import model_to_dict
#         # for good in goods:
#         #     json_dict = model_to_dict(good)
#         #     json_list.append(json_dict)
#
#         from django.http import HttpResponse,JsonResponse
#         from django.core import serializers
#         import json
#
#         json_data = serializers.serialize('json',goods)
#         json_data = json.loads(json_data)
#         # 返回json，一定要指定类型content_type='application/json'
#         # return HttpResponse(json.dumps(json_list), content_type='application/json')
#         return JsonResponse(json_data, safe=False)