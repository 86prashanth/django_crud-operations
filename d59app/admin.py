from django.contrib import admin
from .models import Add
# Register your models here.
@admin.register(Add)
class Addadmin(admin.ModelAdmin):
    list_display=('id','name','email','password')