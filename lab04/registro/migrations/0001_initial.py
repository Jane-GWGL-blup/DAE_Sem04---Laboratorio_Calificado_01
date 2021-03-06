# Generated by Django 4.0.3 on 2022-04-05 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_region', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('candidatura', models.CharField(max_length=60)),
                ('ideologia', models.CharField(max_length=100)),
                ('edad', models.IntegerField(default=0)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.region')),
            ],
        ),
    ]
