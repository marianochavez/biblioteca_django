# Generated by Django 3.1.7 on 2021-03-23 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0009_auto_20210322_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]