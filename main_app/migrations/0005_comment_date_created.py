# Generated by Django 4.1.5 on 2023-01-24 01:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_comment_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 24, 1, 0, 53, 57720, tzinfo=datetime.timezone.utc)),
        ),
    ]