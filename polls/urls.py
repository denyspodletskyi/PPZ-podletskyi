from django.urls import path
from . import views
from django.urls import path
from .views import get_questions

app_name = 'polls'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('', get_questions),
]

