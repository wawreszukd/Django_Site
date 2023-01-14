from django.urls import include, path
from . import views
app_name="container"
urlpatterns = [
    path("",views.index,name='container')
]