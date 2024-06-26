# Generated by Django 5.0.6 on 2024-05-14 07:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_cart_product_alter_priceupdate_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='added',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='priceupdate',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='profile',
            name='dateRegistered',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='delivery_status',
            field=models.CharField(choices=[('ACCEPTED', 'Accepted'), ('RECEIVED', 'Received'), ('IN_TRANSIT', 'In Transit'), ('OUT_FOR_DELIVERY', 'Out for Delivery'), ('CANCELLED', 'Cancelled')], default='ACCEPTED', max_length=20),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
