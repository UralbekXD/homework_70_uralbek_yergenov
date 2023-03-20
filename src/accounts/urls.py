from django.urls import path

from .views import *


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('create/', RegisterView.as_view(), name='register'),
]
