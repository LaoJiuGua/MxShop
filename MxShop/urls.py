"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
import xadmin
from django.urls import path,include

from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken import views

from django.views.static import serve
from rest_framework_jwt.views import obtain_jwt_token

from MxShop.settings import MEDIA_ROOT


urlpatterns = [
    path('adminx/', xadmin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    path('api-token-auth',views.obtain_auth_token),
    path('login/',obtain_jwt_token),
    path('ueditor/', include('DjangoUeditor.urls')),
    path('goods/', include('goods.urls')),
    path('users/', include('users.urls')),
    path('oper/', include('user_operation.urls')),
    path('media/<path:path>',serve,{'document_root':MEDIA_ROOT}),
    path('docs',include_docs_urls(title='仙剑奇侠传')),
]
