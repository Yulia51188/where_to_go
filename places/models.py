from django.db import models
from tinymce.models import HTMLField


class PlacePhoto(models.Model):
    image = models.ImageField('Фотография')
    index = models.IntegerField('Порядковый номер', blank=True, null=True)
    place = models.ForeignKey(
        'Place',
        verbose_name='Место',
        related_name='photos',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.place.title} #{self.index}'    

    class Meta:
        ordering = ['index']


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Краткое описание', blank=True)
    description_long = HTMLField('Подробное описание', blank=True)
    latitude = models.FloatField('Широта')
    longitude = models.FloatField('Долгота')
    slug = models.SlugField('Идентификатор места', unique=True)

    def __str__(self):
        return f'{self.title} ({self.longitude}, {self.latitude})'

    class Meta():
        unique_together = [['title', 'slug', 'latitude', 'longitude']]
