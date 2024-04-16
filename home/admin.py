from django.contrib import admin
from .models import*

class HotelAdmin(admin.ModelAdmin):
    list_display=['hotel_name','hotel_price','hotel_description']


# Register your models here.
admin.site.register(Hotel ,HotelAdmin)
admin.site.register(HotelImage)
admin.site.register(Amenitites)