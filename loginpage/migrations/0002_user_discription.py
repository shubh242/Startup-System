# Generated by Django 3.1.7 on 2021-03-19 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='discription',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]