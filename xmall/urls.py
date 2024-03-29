"""xmall URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from account.views import UserViewSet
from cart.views import CartViewSet, CartEditView
from home.views import NavListView
from order.views import OrderViewSet
from xmall import settings

router = DefaultRouter()
# router.register(r'user', UserViewSet, basename='user')
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'order', OrderViewSet, basename='order')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/cart/editCheckAll/', CartEditView.as_view()),
    path('api/', include(router.urls)),
    path('api-auth/', include("rest_framework.urls")),
    path('api/goods/', include(('goods.urls', 'goods'), namespace='goods')),
    path('api/user/', include(('account.urls', 'account'), namespace='account')),
    path('api/home/', include(('home.urls', 'home'), namespace='home')),
    path('api/navlist/', NavListView.as_view()),
    path('api/address/', include(('address.urls', 'address'), namespace='address')),
    # path('api/cart/cartEdit/', include(('cart.urls', 'cart'), namespace='cart')),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('api/api-token-auth/', obtain_auth_token),
    path('api/api-token-auth/', obtain_jwt_token),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
