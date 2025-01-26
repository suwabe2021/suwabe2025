from django.urls import path
from . import views

app_name ="login"
urlpatterns = [
    path("", views.index, name='index_view'),
    path("<str:passwd>/", views.authentication, name='authentication'),
]