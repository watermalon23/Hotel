# Generated by Django 5.0.1 on 2024-04-13 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='update_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='hotelimage',
            name='update_at',
            field=models.DateField(auto_now=True),
        ),
    ]