# Generated by Django 3.1.8 on 2021-09-23 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_products_catid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='catid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='accounts.category'),
        ),
    ]
