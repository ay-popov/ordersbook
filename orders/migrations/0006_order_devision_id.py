# Generated by Django 4.1.2 on 2022-11-13 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_devision'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='devision_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='order', to='orders.devision'),
        ),
    ]