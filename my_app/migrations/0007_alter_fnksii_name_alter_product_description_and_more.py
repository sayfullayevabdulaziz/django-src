# Generated by Django 4.1.1 on 2022-10-28 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_product_img_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fnksii',
            name='name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.CreateModel(
            name='Technique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.product')),
            ],
        ),
    ]
