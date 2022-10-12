from django.urls import path
from .views import *

urlpatterns = [
    path('',add_show,name='home'),
    path('<int:id>/',update_data,name='update'),
    path('delete/<int:id>/',update_data,name='deletedata'),
]
