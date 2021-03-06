# Generated by Django 3.2 on 2021-12-09 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_placephoto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='placephoto',
            options={'ordering': ['index']},
        ),
        migrations.AddField(
            model_name='placephoto',
            name='index',
            field=models.IntegerField(default=0, verbose_name='Порядковый номер'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='placephoto',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Фотография'),
        ),
    ]
