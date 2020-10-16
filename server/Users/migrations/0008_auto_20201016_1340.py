# Generated by Django 3.1.2 on 2020-10-16 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20201016_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='processorpoint',
            name='name',
            field=models.CharField(default='ChargSpot1', max_length=50, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chargespot',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]