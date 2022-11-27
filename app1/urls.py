from django.urls import path, include
from app1 import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

    
    path('',views.home,name="home"),
    path('add_land/',views.addland,name='addland'),
    path('add_plot/',views.addplot,name='addplot'),

    
    
]