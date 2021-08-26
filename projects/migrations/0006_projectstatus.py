# Generated by Django 3.2.6 on 2021-08-24 15:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0002_alter_status_options'),
        ('projects', '0005_alter_project_slug_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projects.project')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='status.status')),
            ],
        ),
    ]
