# Generated by Django 3.0.4 on 2020-03-25 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='title',
            field=models.CharField(default='Just another skill', max_length=200),
        ),
    ]