from django.contrib import admin
from django.urls import include,path
from admission import views
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    #path("welcome/",views.welcome),
    #path("",views.colleges),
    #path('',home,name='home'),
]
