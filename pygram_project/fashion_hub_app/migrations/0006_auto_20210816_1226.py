# Generated by Django 3.1.7 on 2021-08-16 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashion_hub_app', '0005_auto_20210724_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='subcategory',
            field=models.CharField(choices=[('Men-T-Shirts', 'Men-T-Shirts'), ('Women-T-Shirts', 'Women-T-Shirts'), ('Shirts', 'Shirts'), ('Men-Jeans', 'Men-Jeans'), ('Women-Jeans', 'Women-Jeans'), ('Men-Watches', 'Men-Watches'), ('Women-Watches', 'Women-Watches'), ('Saree', 'Saree'), ('Churidhar', 'Churidhar'), ('boys', 'boys'), ('girls', 'girls')], default='1', max_length=50),
        ),
    ]
