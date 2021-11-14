# Generated by Django 3.1.7 on 2021-09-13 17:26

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0006_delete_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orderz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('mobile', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=15)),
                ('state', models.CharField(choices=[('Kerala', 'Kerala'), ('Tamilnaadu', 'Tamilnaadu'), ('Telangana', 'telangana')], default='1', max_length=25)),
                ('pin', models.IntegerField()),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('order_status', models.CharField(choices=[('order recieved', 'order recieved'), ('order processing', 'order processing'), ('on the way', 'on the way'), ('order cancelled', 'order cancelled')], max_length=25)),
                ('cartt', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Cart.items')),
            ],
        ),
    ]
