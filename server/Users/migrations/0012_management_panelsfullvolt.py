# Generated by Django 3.1.2 on 2020-10-16 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20201016_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='management',
            name='panelsFullVolt',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
            preserve_default=False,
        ),
    ]
