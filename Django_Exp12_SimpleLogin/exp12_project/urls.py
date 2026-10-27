from django.contrib import admin
from django.urls import path
from auth_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('welcome/', views.welcome_view, name='welcome'),
    path('logout/', views.logout_view, name='logout'),
]
