# Generated by Django 4.1.13 on 2024-06-19 00:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_rename_order_created_bf319d_idx_order_created_047412_idx_and_more'),
    ]

    operations = [
        migrations.RenameIndex(
            model_name='order',
            new_name='orders_created_e28e23_idx',
            old_name='order_created_047412_idx',
        ),
        migrations.AlterModelTable(
            name='order',
            table='orders',
        ),
    ]
