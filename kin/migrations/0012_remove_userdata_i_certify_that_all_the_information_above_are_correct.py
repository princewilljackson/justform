# Generated by Django 3.0.4 on 2020-11-20 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kin', '0011_auto_20201120_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='I_certify_that_all_the_information_above_are_correct',
        ),
    ]