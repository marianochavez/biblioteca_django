# Generated by Django 3.1.6 on 2021-03-17 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0003_auto_20210317_1147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autor',
            name='descripcion',
        ),
    ]
