
from django.urls import path
from . import views


app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile_list/', views.profile_list, name='profile_list'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('logout', views.logout_user, name='logout'),
    path('login', views.login_user, name='login'),
    path('signup', views.sign_up, name='sign_up'),
]