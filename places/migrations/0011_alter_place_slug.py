# Generated by Django 3.2 on 2021-12-22 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0010_alter_placephoto_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Идентификатор места'),
        ),
    ]
