
from django.urls import path
from .views import *
urlpatterns = [
    path("",getData,name="getData"),
    path("create/",createData,name="createData"),
    path("update/<int:id>",UpdateData,name="UpdateData"),
    path("person/<int:id>/delete",DeleteData,name="DeleteData"),
]