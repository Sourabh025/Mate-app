# Generated by Django 2.2.5 on 2020-05-14 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20200511_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='desription',
            field=models.TextField(default=None),
        ),
    ]
