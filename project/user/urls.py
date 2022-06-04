from django.urls import path
from user import views as user_views

app_name = 'user'
urlpatterns = [
    path('register/', user_views.register, name='register'),
    path('login/', user_views.login, name='login'),
    path('logout/', user_views.logout, name='logout')
]