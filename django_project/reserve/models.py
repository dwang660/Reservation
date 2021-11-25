from django.db import models

# Create your models here.
class reserve(models.Model):
  reservation_id= models.IntegerField(max_length=10)
  number_adult= models.IntegerField(max_length=10)
  number_kids= models.IntegerField(max_length=10)
  table_id_1= models.IntegerField(max_length=10)
  table_id_2= models.IntegerField(max_length=10)
  name= models.CharField(max_length=50)
  phone= models.IntegerField(max_length=10)
  reservation_time= models.TimeField()
  def __str__(self):
      return f"(self.title)"