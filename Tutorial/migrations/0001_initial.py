# Generated by Django 3.1.2 on 2021-03-19 06:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutorial_title', models.TextField(blank=True)),
                ('tutorial_description', models.TextField(blank=True)),
                ('tutorial_tags', models.TextField(blank=True)),
                ('tutorial_video', models.FileField(upload_to='videos')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('tutorial_uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
