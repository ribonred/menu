# Generated by Django 2.0 on 2019-08-05 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20190805_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(editable=False, max_length=255),
        ),
    ]