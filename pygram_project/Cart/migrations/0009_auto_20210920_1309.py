# Generated by Django 3.1.7 on 2021-09-20 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0008_auto_20210914_2205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderz',
            name='cartt',
        ),
        migrations.AddField(
            model_name='orderz',
            name='cartt',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Cart.items'),
            preserve_default=False,
        ),
    ]
