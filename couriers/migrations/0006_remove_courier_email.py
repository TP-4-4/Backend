# Generated by Django 4.1.13 on 2024-06-19 00:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('couriers', '0005_alter_courier_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courier',
            name='email',
        ),
    ]
