# Generated by Django 3.1.8 on 2021-10-17 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_order_orderproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='deliverystatus',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='deliverytime',
            field=models.DateTimeField(null=True),
        ),
    ]