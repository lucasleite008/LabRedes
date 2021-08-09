from django.urls import path

from .views import *

urlpatterns = [
    path('', Dash.as_view(), name='dash'),
]