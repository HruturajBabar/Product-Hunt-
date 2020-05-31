from django.contrib import admin
from django.urls import path, include
from Products import views
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name = 'home'),
    path('accounts/',include('Accounts.urls')),
    path('products/',include('Products.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
