# Generated by Django 2.2.5 on 2019-09-27 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_user_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='active',
        ),
    ]
