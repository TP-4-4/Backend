# Generated by Django 4.1.13 on 2024-06-19 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameIndex(
            model_name='category',
            new_name='Category_name_476266_idx',
            old_name='shop_catego_name_289c7e_idx',
        ),
        migrations.RenameIndex(
            model_name='product',
            new_name='Product_id_add86e_idx',
            old_name='shop_produc_id_f21274_idx',
        ),
        migrations.RenameIndex(
            model_name='product',
            new_name='Product_name_5f5d5c_idx',
            old_name='shop_produc_name_a2070e_idx',
        ),
        migrations.RenameIndex(
            model_name='product',
            new_name='Product_created_e1c2c8_idx',
            old_name='shop_produc_created_ef211c_idx',
        ),
        migrations.AlterModelTable(
            name='category',
            table='Category',
        ),
        migrations.AlterModelTable(
            name='product',
            table='Product',
        ),
    ]