# Generated by Django 4.1.1 on 2022-10-28 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0009_alter_technique_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technique',
            name='age',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
