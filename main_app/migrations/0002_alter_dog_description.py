# Generated by Django 4.1.5 on 2023-01-27 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
# Generated by Django 4.1.5 on 2023-01-27 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]