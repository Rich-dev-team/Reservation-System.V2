from django.urls import path, include, re_path
from . import views
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static

urlpatterns = [
    path('LoginPortal/', views.login_portal,),
    path('StaffLogin/',views.staff_login,),


    
]


