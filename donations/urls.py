from django.urls import path
from . import views 
# from .views import donate, confirm, success, failure, khalti_confirm, khalti_verify


app_name = 'donations'
urlpatterns = [
    path("donate/", views.donate, name="donate"),
    path("confirm/<uuid:uuid>/", views.confirm, name="donation_confirm"),
    path("success/<uuid:uuid>/", views.success, name="donation_success"),
    path("failure/<uuid:uuid>/", views.failure, name="donation_failure"),

    path("khalti/confirm/<uuid:uuid>/", views.khalti_confirm, name="khalti_confirm"),
    path("khalti/verify/<uuid:uuid>/", views.khalti_verify, name="khalti_verify"),
]
