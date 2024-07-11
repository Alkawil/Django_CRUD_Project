from django.db import models


# Create your models here.
class DrinksCategory(models.Model):
    category_name = models.CharField(max_length=200)
# Create model Drinks
class Drinks(models.Model):
    drink = models.CharField(max_length=200)
    price = models.IntegerField()
    category_id = models.ForeignKey(DrinksCategory, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.drink

class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_count = models.IntegerField()
    reservation_time = models.DateField()
    comments= models.CharField(max_length=1000)

