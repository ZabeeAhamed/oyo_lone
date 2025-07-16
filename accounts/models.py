from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class HotelUser(User):
    profile_picture=models.ImageField(upload_to="profiles")
    phone_number=models.CharField(unique=True)
    email_token=models.CharField(max_length=100,null=True,blank=True)
    otp=models.CharField(max_length=10 ,null=True,blank=True)
    is_verified = models.BooleanField(default = False)

class HotelVendor(User):
    profile_picture=models.ImageField(upload_to="profiles")
    business_name = models.CharField(max_length = 100)
    phone_number=models.CharField(unique=True)
    email_token=models.CharField(max_length=100,null=True,blank=True)
    otp=models.CharField(max_length=10 ,null=True,blank=True)
    is_verified = models.BooleanField(default = False)

class Ameneties(models.Model):
    name=models.CharField(max_length=1000)
    icon=models.ImageField(upload_to="hotels")

    def __str__(self) -> str:
        return self.name

class Hotel(models.Model):
    hotel_name=models.CharField(max_length=100)
    hotel_description=models.TextField()
    hotel_slug=models.SlugField(max_length=1000,unique=True)
    hotel_price=models.FloatField()
    hotel_offer_price=models.FloatField()
    hotel_owner=models.ForeignKey(HotelVendor,on_delete=models.CASCADE,related_name="hotels")
    ameneties=models.ManyToManyField(Ameneties)
    hotel_locations=models.TextField()
    is_active=models.BooleanField(default=True)

class HotelImages(models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name="hotel_images")
    image=models.ImageField(upload_to="hotels")
class HotelManager(models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name="hotel_managers")
    manager_name=models.CharField(max_length=100)
    manager_contact=models.CharField(max_length=100)
class Booking(models.Model):
    user = models.ForeignKey(HotelUser, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, related_name="bookings", on_delete=models.CASCADE)
    booking_start_date = models.DateField()
    booking_end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.hotel.hotel_name}"