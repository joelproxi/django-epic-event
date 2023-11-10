# Generated by Django 4.2.5 on 2023-11-07 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
