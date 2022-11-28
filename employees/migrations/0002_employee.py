# Generated by Django 4.1.2 on 2022-10-22 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=64)),
                ('firstname', models.CharField(max_length=64)),
                ('patronymic', models.CharField(max_length=64)),
                ('personnel_number', models.CharField(max_length=64, unique=True)),
                ('email', models.CharField(max_length=64)),
            ],
        ),
    ]
