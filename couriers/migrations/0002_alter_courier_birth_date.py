# Generated by Django 4.1.13 on 2024-06-18 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('couriers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courier',
            name='birth_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
