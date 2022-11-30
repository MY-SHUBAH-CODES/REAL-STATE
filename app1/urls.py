from django.urls import path, include
from app1 import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

    
    path('',views.home,name="home"),
    path('add_land/',views.addland,name='addland'),
    path('add_plot/',views.addplot,name='addplot'),
    path('allland/',views.allland,name='allland'),
    path('allland/<int:pk>/',views.landdetails,name='landdetails'),
    path('allplot/',views.allplot,name='allplot'),
    path('allplot/<int:pk>/',views.plotdetails,name='plotdetails'),
    path('contact/',views.contact,name='contact'),
    path('developer/',views.developer,name='developer'),









    
    
]
