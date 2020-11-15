# Generated by Django 3.1 on 2020-11-15 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resto', '0001_initial'),
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='resto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='resto_category', to='resto.restaurant'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='resto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='resto_products', to='resto.restaurant'),
            preserve_default=False,
        ),
    ]
