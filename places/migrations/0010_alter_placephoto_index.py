# Generated by Django 3.2 on 2021-12-22 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_alter_place_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placephoto',
            name='index',
            field=models.IntegerField(blank=True, null=True, verbose_name='Порядковый номер'),
        ),
    ]
