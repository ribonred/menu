# Generated by Django 2.0 on 2019-08-06 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_auto_20190805_2302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='Category',
        ),
    ]