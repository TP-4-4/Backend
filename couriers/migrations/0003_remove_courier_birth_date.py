# Generated by Django 4.1.13 on 2024-06-18 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('couriers', '0002_alter_courier_birth_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courier',
            name='birth_date',
        ),
    ]
