# Generated by Django 3.1.2 on 2020-10-22 10:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20201022_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chargehistory',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
