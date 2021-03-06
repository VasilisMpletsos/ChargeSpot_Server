# Generated by Django 3.1.2 on 2020-10-15 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='country',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='prefersDark',
            field=models.BooleanField(default='False'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nickname',
            field=models.CharField(default='', max_length=40),
        ),
    ]
