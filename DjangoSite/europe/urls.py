from django.urls import path
from . import views
app_name="europes"
urlpatterns = [
    path("",views.index,name='europe')
]