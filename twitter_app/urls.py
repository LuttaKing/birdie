from django.urls import path
from . import views

urlpatterns = [
    path('update_id', views.update_last_id,),

]