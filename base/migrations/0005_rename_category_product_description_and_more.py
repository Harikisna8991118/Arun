# Generated by Django 4.1.2 on 2022-10-26 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_rename_name_product_product_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_name',
            new_name='name',
        ),
    ]
