from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve


urlpatterns = [
    path('',views.index,name = "index"),
    # path('View_all_data',views.View_all_data,name = "View_all_data"),
    path('get_timeinterval',views.get_timeinterval,name = "get_timeinterval")
]
