from django.urls import path

from hello import views

urlpatterns = [
    path("application-data/", views.application_data_view, name="application_data"),
    path("user-data/", views.user_data_view, name="user_data"),
]
