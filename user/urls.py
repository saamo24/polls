from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('', views.login, name='login1'),
    path('s', views.login_view, name='login'),
]
