# Generated by Django 3.0.4 on 2020-11-20 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kin', '0010_auto_20201120_1729'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='I_affirm_and_certify_that_all_the_information_above_are_correct',
            new_name='I_certify_that_all_the_information_above_are_correct',
        ),
    ]
