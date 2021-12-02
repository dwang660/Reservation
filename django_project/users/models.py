from django.db import models
from django.contrib.auth.models import User
from address.models import AddressField
from phonenumber_field.modelfields import PhoneNumberField
from table.models import Table
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = PhoneNumberField(null=False, blank=True, unique=False, region="US")
    mailing_addresss = AddressField(related_name="mailing_address", null=True)
    billing_addresss = AddressField(related_name="billing_address", null=True)
    points = models.IntegerField(null=True)
    prefer_table = models.OneToOneField(Table, on_delete=models.CASCADE, null=True)
    prefer_payment = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
