from django.urls import path

from .views import (
    IndexView)

app_name = 'users'

urlpatterns = [
    path('<str:page>/', IndexView.as_view(), name='index'),
    path('<str:page>/<str:subpage>/', IndexView.as_view(), name='index'),
    path('<str:page>/<str:subpage>/<str:subpage2>/', IndexView.as_view(), name='index'),
    path('', IndexView.as_view(), name='index'),
]
