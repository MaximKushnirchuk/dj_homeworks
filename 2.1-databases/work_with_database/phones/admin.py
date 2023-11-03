from django.contrib import admin
from phones.models import Phone


# Register your models here.

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display= ['name', 'slug']
    list_filter= ['slug']
    