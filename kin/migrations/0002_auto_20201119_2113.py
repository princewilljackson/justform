# Generated by Django 3.0.4 on 2020-11-19 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userform',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='userform',
            name='relationship',
        ),
        migrations.AlterField(
            model_name='userform',
            name='phone',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userform',
            name='ssn',
            field=models.CharField(max_length=100),
        ),
    ]