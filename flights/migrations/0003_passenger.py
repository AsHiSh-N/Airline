# Generated by Django 3.1.6 on 2021-02-22 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_auto_20210222_0841'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=25)),
                ('last', models.CharField(max_length=15)),
            ],
        ),
    ]
