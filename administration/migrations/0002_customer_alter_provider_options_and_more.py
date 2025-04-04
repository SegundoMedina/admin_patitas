# Generated by Django 5.1.3 on 2024-11-27 23:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=128)),
            ],
        ),
        migrations.AlterModelOptions(
            name='provider',
            options={'verbose_name': 'Paseador', 'verbose_name_plural': 'Paseadores'},
        ),
        migrations.AlterField(
            model_name='provider',
            name='description',
            field=models.TextField(verbose_name='Describe al paseador'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='first_name',
            field=models.CharField(max_length=128, verbose_name='Nombres'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='last_name',
            field=models.CharField(max_length=128, verbose_name='Apellidos'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='main_photo',
            field=models.ImageField(blank=True, null=True, upload_to='provider/', verbose_name='Selecciona tu foto'),
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('age', models.CharField(max_length=64)),
                ('pedigree', models.CharField(max_length=128)),
                ('main_photo', models.ImageField(blank=True, null=True, upload_to='pets/')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='administration.customer')),
            ],
        ),
    ]
