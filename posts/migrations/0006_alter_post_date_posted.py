# Generated by Django 4.2.3 on 2023-07-05 12:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Date_Posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 5, 13, 24, 52, 939654)),
        ),
    ]
