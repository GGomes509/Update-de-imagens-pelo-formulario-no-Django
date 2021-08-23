from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name='produtos'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.base, name='base'),
    path('', views.home, name='home' ),
    path('index/', views.index, name='index')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)