# Generated by Django 3.0.4 on 2020-11-20 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kin', '0009_userdata_i_affirm_and_certify_that_all_the_information_above_are_correct'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='contact',
            new_name='Current_Address',
        ),
        migrations.AlterField(
            model_name='userdata',
            name='I_affirm_and_certify_that_all_the_information_above_are_correct',
            field=models.BooleanField(),
        ),
    ]
