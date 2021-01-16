# Generated by Django 3.1 on 2021-01-16 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resto', '0001_initial'),
        ('menu', '0002_auto_20201115_1541'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='Product',
            new_name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='no_tlp',
        ),
        migrations.AddField(
            model_name='order',
            name='table',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='order_table', to='resto.table'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products_category', to='menu.category'),
        ),
    ]
