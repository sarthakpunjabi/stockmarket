"""
This contains urls for tracking urls
"""
from django.urls import path
from . import views

urlpatterns = [
    path('',views.stockPicker,name='stockpicker'),
    path('stoctracker/',views.stockTracker,name='stocktracker'),
    path('stoctracker/<str:key>',views.getnews,name='stocktracker-news'),
    path('sendmessage/',views.fullnews,name='send-message'),
    path('getaffirmation/<str:news>',views.getaffirmation,name='get-affirmation')

]