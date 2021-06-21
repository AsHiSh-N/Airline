# Generated by Django 3.1.6 on 2021-02-24 04:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0004_passenger_flights'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
