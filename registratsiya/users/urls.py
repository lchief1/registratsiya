from django.urls import path
from .views import user_list, user_create

app_name = 'users'
urlpatterns = [
    path('', user_list, name='user_list'),
    path('new/', user_create, name='user_create'),
]
