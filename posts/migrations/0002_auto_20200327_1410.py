# Generated by Django 3.0.4 on 2020-03-27 14:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='date_of_birth',
            field=models.DateField(default=datetime.date(1970, 1, 1)),
        ),
    ]