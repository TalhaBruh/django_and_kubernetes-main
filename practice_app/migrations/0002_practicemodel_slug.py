# Generated by Django 5.1 on 2024-08-26 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='practicemodel',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
