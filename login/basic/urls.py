from django.urls import path
from . import views

app_name = 'basic'

urlpatterns = [
    path('', views.homepage, name='home'),
    path('login/', views.login_page, name='login'),
    path('registration/', views.register, name='register'),
    path('logout/', views.logout_page, name='logout')
]