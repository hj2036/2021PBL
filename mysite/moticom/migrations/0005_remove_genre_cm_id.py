# Generated by Django 3.2.6 on 2021-10-25 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moticom', '0004_auto_20210807_0103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='cm_id',
        ),
    ]