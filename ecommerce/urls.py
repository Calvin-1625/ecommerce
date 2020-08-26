"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, re_path, include
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView


from carts.views import cart_home
from addresses.views import checkout_address_create_view
from accounts.views import login_page, register_page, guest_register_view
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page, name = 'home'),
    path('about/',views.about, name = 'about'),
    path('contact/',views.contact, name = 'contact'),
    path('login/',login_page, name = 'login'),
    path('checkout/address/create/',checkout_address_create_view, name = 'checkout_address_create'),
    path('register/guest',guest_register_view, name = 'guest_register'),
    path('logout/',LogoutView.as_view(), name = 'logout'),
    path('register/',register_page, name = 'register'),
    path('bootstrap/',TemplateView.as_view(template_name ='bootstrap/example.html')),
    # path('featured/',ProductFeaturedListView.as_view(), name = 'featured'),
    # re_path(r'^featured/(?P<pk>\d+)/$',ProductFeaturedDetailView.as_view(), name = 'featured_detail'),
    path('products/', include(("products.urls", 'products'), namespace='products')),
    path('search/', include(("search.urls", 'search'), namespace='search')),
    path('cart/',cart_home, name = 'cart'),
    path('cart/', include(("carts.urls", 'cart'), namespace='cart')),
    # path('products-fbv/',product_list_view, name = 'product-fbv'),
    # #re_path(r'^product/(?P<pk>\d+)/$',ProductDetailView.as_view(), name = 'detail'),
    # re_path(r'^products-fbv/(?P<pk>\d+)/$',product_detail_view, name = 'detail'),
    # re_path(r'^products/(?P<slug>[\w-]+)/$',ProductDetailSlugView.as_view(), name = 'detail_slug'),
    # #re_path(r'^article/(?P<slug>[\w-]+)/$', article_detail, name='article'),
    
]

# app_name = 'products'

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)