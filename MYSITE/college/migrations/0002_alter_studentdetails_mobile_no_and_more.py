# Generated by Django 4.0 on 2021-12-18 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetails',
            name='mobile_no',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='mobile_no',
            field=models.CharField(max_length=10),
        ),
    ]