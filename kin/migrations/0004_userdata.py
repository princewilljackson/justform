# Generated by Django 3.0.4 on 2020-11-20 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kin', '0003_auto_20201120_1333'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('middlename', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('relationship', models.CharField(choices=[('father', 'Father'), ('mother', 'Mother'), ('husband', 'Husband'), ('wife', 'Wife'), ('son', 'Son'), ('daughter', 'Daughter')], max_length=8)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=12)),
                ('ssn', models.CharField(max_length=10)),
                ('contact', models.TextField()),
            ],
        ),
    ]
