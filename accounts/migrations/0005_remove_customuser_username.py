# Generated by Django 4.2.5 on 2023-11-07 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_customuser_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
    ]
