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


def load_place(place_url):
    response = requests.get(place_url)
    response.raise_for_status()
    return response.json()


def read_file(file_path):
    with open(file_path, 'r') as file_obj:
        content = file_obj.read()
    return json.loads(content)


def load_places(folder_path):
    places_paths = [os.path.join(folder_path, filename)
                    for filename in os.listdir(folder_path)]
    places = [read_file(file_path) for file_path in places_paths]
    return places


def create_place_entity(place, slug):    
    place_entity, created = Place.objects.get_or_create(
        title=place['title'],
        description_short=place['description_short'],
        description_long=place['description_long'],
        latitude=place['coordinates']['lat'],
        longitude=place['coordinates']['lng'],
        slug=slug,
    )

    place_photos = place_entity.photos.all()
    if place_photos.exists():
        place_photos.delete()

    upload_photos(place['imgs'], place_entity)


def upload_photos(photo_urls, place):
    for photo_url in photo_urls:
        response = requests.get(photo_url)
        response.raise_for_status()

        place_photos = PlacePhoto.objects.filter(place=place)

        if not place_photos.exists():
            last_index = 0
        else:
            last_index = (place_photos.order_by('-index'))[0].index
        
        photo = ContentFile(response.content)
        new_photo, created = PlacePhoto.objects.get_or_create(
            place=place,
            index=last_index + 1,
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
        parser.add_argument('--place_slug', type=str, default='place')
        parser.add_argument('-f', '--load_from_folder', action='store_true')

    def handle(self, *args, **options):
        if options['load_from_folder']:
            places = load_places(options['file_url'])
            for place in places:
                print(place)
                create_place_entity(place, options['place_slug'])
        else:
            place = load_place(options['file_url'])
            create_place_entity(place, options['place_slug'])
