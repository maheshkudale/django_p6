# Generated by Django 3.2.12 on 2022-03-07 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_product_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='customer',
        ),
        migrations.AddField(
            model_name='product',
            name='customer',
            field=models.ManyToManyField(related_name='product', to='users.Customer'),
        ),
    ]
