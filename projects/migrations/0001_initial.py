# Generated by Django 3.2.6 on 2021-08-24 10:20

import datetime
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
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('dead_line', models.DateField()),
                ('created_date', models.DateField(default=datetime.datetime(2021, 8, 24, 12, 20, 46, 797622))),
            ],
        ),
    ]
