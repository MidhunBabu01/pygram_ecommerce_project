# Generated by Django 3.1.7 on 2021-11-13 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fashion_hub_app', '0008_auto_20210817_2100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='available',
        ),
    ]
