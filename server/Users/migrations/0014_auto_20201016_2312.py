# Generated by Django 3.1.2 on 2020-10-16 20:12

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_userprofile_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='account',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=4),
        ),
    ]
