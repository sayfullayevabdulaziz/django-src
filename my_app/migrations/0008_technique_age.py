# Generated by Django 4.1.1 on 2022-10-28 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0007_alter_fnksii_name_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='technique',
            name='age',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]