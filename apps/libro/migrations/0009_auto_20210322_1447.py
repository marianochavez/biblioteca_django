# Generated by Django 3.1.7 on 2021-03-22 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0008_autor_estado'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'ordering': ['id'], 'verbose_name': 'Autor', 'verbose_name_plural': 'Autores'},
        ),
    ]
