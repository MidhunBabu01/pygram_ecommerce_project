# Generated by Django 3.1.7 on 2021-11-11 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0007_adminproducts_imgg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminproducts',
            name='img1',
        ),
        migrations.RemoveField(
            model_name='adminproducts',
            name='img2',
        ),
        migrations.RemoveField(
            model_name='adminproducts',
            name='img3',
        ),
    ]
