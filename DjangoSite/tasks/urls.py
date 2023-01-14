from django.urls import path
from . import views
app_name="tasks"
urlpatterns = [
    path("",views.index,name="tasks"),
    path("add",views.add,name="add"),
    path("delete/<int:id>",views.delete, name="delete")
]