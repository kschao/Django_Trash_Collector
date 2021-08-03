from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.create, name='register'),
    path('weekly_pickup_day', views.weekly_pickup_day, name='weekly_pickup_day'),
    path('one_time_pickup', views.one_time_pickup, name='one_time_pickup'),
    path('suspend_start', views.suspend_start, name='suspend_start'),
    path('balance', views.balance, name='balance')
]
