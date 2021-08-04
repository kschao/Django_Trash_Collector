from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.create, name='register'),
    path('change_pickup_day/', views.change, name='change_pickup_day'),
    path('one_time_pickup/', views.one_time_pickup, name='one_time_pickup'),
    path('suspend_start/', views.suspension_request, name='suspend_start'),
    path ('detail/', views.detail, name='detail')
]
