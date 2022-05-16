from django.urls import path, include
from django.contrib import admin
from . import views
from .views import GeneratePdf

app_name = 'myapp'

urlpatterns = [

    path('',views.hello),
    path('hellopdf/', GeneratePdf.as_view())

]
