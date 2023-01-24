from django.contrib import admin
from django.urls import include, path
from gsdashboard.views import *

urlpatterns = [
    path('gstracking/', include('gstracking.urls')),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]