from django.db import models
import random
# Create your models here.
class reserves(models.Model):
  Reservee_Last_name= models.CharField(max_length=50)
  Reservee_First_name= models.CharField(max_length=50)
  number_of_adult= models.IntegerField(max_length=10)
  number_of_kids= models.IntegerField(max_length=10)
  table_id= models.CharField(max_length=3)
  Tele_Num= models.IntegerField(max_length=10)
  Reservation_Date= models.DateField()
  Start_Time= models.TimeField()
  End_Time= models.TimeField()
  Reservation_ID= 1234567 

  def __str__(self):
      return f"(self.title)"