# Generated by Django 2.2.5 on 2019-09-27 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='active',
        ),
    ]
