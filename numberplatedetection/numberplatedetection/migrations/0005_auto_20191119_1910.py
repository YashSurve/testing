# Generated by Django 2.2.6 on 2019-11-19 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('numberplatedetection', '0004_auto_20191119_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challan',
            name='mobilenumber',
            field=models.BigIntegerField(),
        ),
    ]