# Generated by Django 2.2.5 on 2020-05-16 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20200516_1524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='extra',
        ),
    ]
