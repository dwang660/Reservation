# Generated by Django 3.2.9 on 2021-11-29 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0003_alter_reservation_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='out',
            field=models.TimeField(null=True),
        ),
    ]