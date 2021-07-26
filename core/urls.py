from django.urls import path
from core.views import home, assignment, service


app_name = "core"


urlpatterns = [
    path("", home, name="home"),
    path("assignment/", assignment, name="assignment"),
    path("service/", service, name="service")    
]
