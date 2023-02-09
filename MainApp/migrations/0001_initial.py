# Generated by Django 4.1.4 on 2023-02-08 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Index_name', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('open', models.FloatField(default=0)),
                ('high', models.FloatField(default=0)),
                ('low', models.FloatField(default=0)),
                ('close', models.FloatField(default=0)),
                ('volume', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files')),
            ],
        ),
        migrations.CreateModel(
            name='Time_interval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_interval', models.CharField(max_length=100)),
            ],
        ),
    ]
