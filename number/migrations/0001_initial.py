# Generated by Django 4.2.5 on 2023-10-05 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('number', models.CharField(max_length=150, unique=True)),
                ('network', models.CharField(choices=[('GLOBE', 'Globe'), ('SMART', 'Smart'), ('TNT', 'TNT'), ('SUN', 'Sun'), ('TM', 'TM'), ('DITO', 'Dito'), ('GOMO', 'Gomo'), ('Not Specified', 'Not Specified')], default='Not Specified', max_length=25)),
                ('load', models.CharField(max_length=150)),
            ],
        ),
    ]
