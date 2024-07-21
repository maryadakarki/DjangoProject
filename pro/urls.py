from django.urls import path
from . import views
from .views import ProCreateView, ProUpdateView

app_name = 'pro'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('create/', ProCreateView.as_view(), name='create'),
    path('update/', ProUpdateView.as_view(), name='update'),
    path('custom_login', views.custom_login, name='custom_login'),

]
