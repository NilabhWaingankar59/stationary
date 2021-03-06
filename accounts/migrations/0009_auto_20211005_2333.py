# Generated by Django 3.1.8 on 2021-10-05 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_products_catid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(default='user_profile1.png', null=True, upload_to='Images/'),
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('cartid', models.AutoField(primary_key=True, serialize=False)),
                ('custid', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.customer')),
            ],
        ),
    ]
