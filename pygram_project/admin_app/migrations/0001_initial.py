# Generated by Django 3.1.7 on 2021-10-23 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('subcategory', models.CharField(choices=[('Men-T-Shirts', 'Men-T-Shirts'), ('Shirts', 'Shirts'), ('Men-Jeans', 'Men-Jeans'), ('Women-Jeans', 'Women-Jeans'), ('Men-Watches', 'Men-Watches'), ('Women-Watches', 'Women-Watches'), ('Saree', 'Saree'), ('Churidhar', 'Churidhar'), ('Top', 'Top'), ('boys', 'boys'), ('girls', 'girls')], default='1', max_length=50)),
                ('img1', models.ImageField(upload_to='pictures')),
                ('img2', models.ImageField(upload_to='pictures')),
                ('img3', models.ImageField(upload_to='pictures')),
                ('desc', models.TextField()),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
