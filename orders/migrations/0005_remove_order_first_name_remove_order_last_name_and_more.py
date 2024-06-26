# Generated by Django 4.1.13 on 2024-06-18 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('couriers', '0003_remove_courier_birth_date'),
        ('orders', '0004_remove_order_address_remove_order_city_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='last_name',
        ),
        migrations.AddField(
            model_name='order',
            name='total_cost',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='order',
            name='courier',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='courier', to='couriers.courier'),
        ),
    ]
