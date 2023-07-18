from django.urls import path
from .views import index

app_name='CORE'
urlpatterns = [
    path('',index,name="index"),
]
