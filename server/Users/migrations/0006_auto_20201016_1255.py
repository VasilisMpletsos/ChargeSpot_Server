# Generated by Django 3.1.2 on 2020-10-16 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20201016_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chargespot',
            name='locationUrl',
            field=models.URLField(),
        ),
    ]
