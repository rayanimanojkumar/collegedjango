# Generated by Django 4.0 on 2021-12-18 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0002_alter_studentdetails_mobile_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetails',
            name='student_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]