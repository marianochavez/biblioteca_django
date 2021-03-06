# Generated by Django 3.1.7 on 2021-03-26 14:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.IntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(1)], verbose_name='Legajo usuario')),
                ('email', models.EmailField(max_length=254, verbose_name='Email de usuario')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre')),
                ('last_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Apellido')),
                ('date_of_birth', models.DateField(null=True, verbose_name='Fecha nacimiento')),
                ('image', models.ImageField(blank=True, max_length=200, null=True, upload_to='perfil/', verbose_name='Imagen de perfil')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
