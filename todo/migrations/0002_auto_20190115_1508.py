# Generated by Django 2.1.5 on 2019-01-15 20:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created',
            field=models.DateField(default=datetime.datetime(2019, 1, 15, 20, 8, 32, 150207, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2019, 1, 15, 20, 8, 32, 150207, tzinfo=utc)),
        ),
    ]