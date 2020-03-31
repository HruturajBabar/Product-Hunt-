from django.contrib import admin
from django.urls import path, include
from Products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name = 'home'),
    path('accounts/',include('Accounts.urls')),
    path('products/',include('Products.urls')),
]
