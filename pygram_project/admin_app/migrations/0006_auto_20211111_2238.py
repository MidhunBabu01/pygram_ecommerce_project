# Generated by Django 3.1.7 on 2021-11-11 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0005_auto_20211111_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminproducts',
            name='img1',
            field=models.ImageField(upload_to='pictures'),
        ),
        migrations.AlterField(
            model_name='adminproducts',
            name='img2',
            field=models.ImageField(upload_to='pictures'),
        ),
        migrations.AlterField(
            model_name='adminproducts',
            name='img3',
            field=models.ImageField(upload_to='pictures'),
        ),
    ]
