# Generated by Django 4.1.13 on 2024-06-19 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_rename_order_created_047412_idx_orders_created_e28e23_idx_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('NOT_ACCEPTED', 'NOT ACCEPTED'), ('ACCEPTED', 'ACCEPTED'), ('CANCELED', 'CANCELED'), ('COMPLETED', 'COMPLETED')], default='NOT_ACCEPTED', max_length=20),
        ),
    ]
