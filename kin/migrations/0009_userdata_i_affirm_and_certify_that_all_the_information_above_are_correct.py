# Generated by Django 3.0.4 on 2020-11-20 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kin', '0008_auto_20201120_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='I_affirm_and_certify_that_all_the_information_above_are_correct',
            field=models.BooleanField(default='False'),
        ),
    ]
