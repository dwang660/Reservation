from django.db import models

# Create your models here.
class reserves(models.Model):
  Reservee_Last_name= models.CharField(max_length=50)
  Reservee_First_name= models.CharField(max_length=50)
  number_of_adult= models.IntegerField(max_length=10)
  numbe_of_kids= models.IntegerField(max_length=10)
  table_id= models.IntegerField(max_length=10)
  Tele_Num= models.IntegerField(max_length=10)
  reservation_time= models.TimeField()
  Reservation_ID= models.IntegerField(max_length=10)

  def __str__(self):
      return f"(self.title)"