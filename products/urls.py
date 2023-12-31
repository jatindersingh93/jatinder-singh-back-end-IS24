"""products URL Configuration

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
from django.conf.urls import url  
from django.urls import path, include, re_path
from django.shortcuts import redirect

from rest_framework import routers
from products_api.views import ProductsView 
from django.conf.urls import url
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from drf_yasg import openapi

# Setup Swagger view
schema_view = get_schema_view(
    openapi.Info(
        title="Product API",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('', lambda req: redirect('doc/')),    
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),     #swagger
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'), #swagger

    path('admin/', admin.site.urls), #admin
    url(r'^api/products$', ProductsView.products_list),  #product listing
    url(r'^api/products/(?P<pk>[0-9]+)$', ProductsView.product_detail), # GET, PUT, POST, DELETE
]
