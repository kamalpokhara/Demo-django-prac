from django.urls import path, include
from . views import *
app_name = "api"

urlpatterns = [
    path("", index, name="home"),
    path("create/", create, name="create"),
    path("detail/<slug:slug>/", detail, name="detail"),
    path("delete/<slug:slug>/", delete, name="delete"),

]
