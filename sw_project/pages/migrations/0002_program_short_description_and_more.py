# Generated by Django 5.1.4 on 2024-12-20 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='short_description',
            field=models.CharField(default='Your default value here', max_length=255),
        ),
        migrations.AddField(
            model_name='scholarship',
            name='short_description',
            field=models.CharField(default='No description provided', max_length=250),
        ),
        migrations.AddField(
            model_name='university',
            name='short_description',
            field=models.CharField(default='Your default value here', max_length=255),
        ),
    ]
