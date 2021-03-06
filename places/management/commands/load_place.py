import json
import os
from urllib.parse import unquote, urlparse

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place, PlacePhoto


def parse_filename(url):
    file_path = unquote(urlparse(url).path)
    return os.path.basename(file_path)


def load_places(folder_path):
    places_paths = [os.path.join(folder_path, filename)
                    for filename in os.listdir(folder_path)]
    places = []
    for file_path in places_paths:                
        with open(file_path, 'r') as file_obj:
            places.append(json.load(file_obj))
    return places


def create_place_entity(place, slug):    
    place_entity, created = Place.objects.get_or_create(
        title=place['title'],
        latitude=place['coordinates']['lat'],
        longitude=place['coordinates']['lng'],
        slug=slug,
        defaults={
            'description_short': place['description_short'],
            'description_long': place['description_long'],
        }
    )

    place_photos = place_entity.photos.all()
    if place_photos.exists():
        place_photos.delete()

    for photo_url in place['imgs']:
        upload_photo(photo_url, place_entity)


def upload_photo(photo_url, place):
    response = requests.get(photo_url)
    response.raise_for_status()
    place_photos_count = PlacePhoto.objects.filter(place=place).count()
    
    photo = ContentFile(response.content)
    new_photo = PlacePhoto.objects.create(
        place=place,
        index=place_photos_count + 1,
    )
    new_photo.image.save(
        parse_filename(photo_url),
        photo,
        save=True
    )


class Command(BaseCommand):
    help = 'Load places from JSON files'

    def add_arguments(self, parser):
        parser.add_argument('file_url', type=str)
        parser.add_argument('--place_slug', type=str, default='')
        parser.add_argument('-f', '--load_from_folder', action='store_true')

    def handle(self, *args, **options):
        if options['load_from_folder']:
            places = load_places(options['file_url'])
            for place in places:
                print(place)
                create_place_entity(place, options['place_slug'])
        else:
            response = requests.get(options['file_url'])
            response.raise_for_status()
            place = response.json()
            create_place_entity(place, options['place_slug'])
