# Generated by Django 5.0.1 on 2024-04-13 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_hotel_update_at_alter_hotelimage_update_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='banner_image',
            field=models.ImageField(upload_to='hotels'),
        ),
    ]