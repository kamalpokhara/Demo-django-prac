from django.urls import path
from . views import *


app_name = 'articles'

urlpatterns = [
    path("", index, name="home"),
    path("create/", create, name="create"),
    path("detail/<slug:slug>/", detail, name="detail"),
    path("update/<slug:slug>/", update, name="update"),
   
    path("article/<slug:slug>/delete/", delete, name='delete'),
]