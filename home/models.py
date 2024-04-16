from django.db import models

# Create your models here.

class Amenitites(models.Model):
    amenity=models.CharField(max_length=100)
    created_at=models.DateField(auto_now_add=True)
    update_at=models.DateField(auto_now_add=True)


    def __str__(self) -> str:
        return self.amenity


class Hotel(models.Model):
    hotel_name=models.CharField(max_length=100)
    hotel_price=models.IntegerField()
    hotel_description=models.TextField()
    amenitites=models.ManyToManyField(Amenitites)
    banner_image=models.ImageField(upload_to="hotels")
    created_at=models.DateField(auto_now_add=True)
    update_at=models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.hotel_name
    
    def get_amenities(self):
        payload=[]

        for amenity in self.amenitites.all():
            payload.append({'id':amenity.id,'amenity':amenity.amenity})
        return payload

class HotelImage(models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="hotels")
    created_at=models.DateField(auto_now_add=True)
    update_at=models.DateField(auto_now=True)


    def __str__(self) -> str:
        return self.hotel.hotel_name

