# Generated by Django 4.1.1 on 2022-11-04 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0011_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
