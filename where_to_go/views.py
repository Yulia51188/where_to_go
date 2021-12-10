from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from places.models import Place


def serialize_place(place):
    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [place.longitude, place.latitude],
        },
        "properties": {
            "title": place.title,
            "placeId": place.slug,
            "detailsUrl": reverse(show_place_details, args=[place.id]),
        }
    }


def serialize_place_details(place):
    return {
        "title": place.title,
        "imgs": [
            photo.image.url for photo in place.photos.all()
        ],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.longitude,
            "lat": place.latitude,
        }
    }


def show_index(request):
    places = Place.objects.prefetch_related('photos').all()

    context = {
        "places_geojson": {
            "type": "FeatureCollection",
            "features": [serialize_place(place) for place in places],
        },

    }

    return render(request, "index.html", context)


def show_place_details(request, place_id):
    place = get_object_or_404(
        Place.objects.prefetch_related('photos'),
        id=place_id
    )
    return JsonResponse(
        serialize_place_details(place),
        json_dumps_params={'indent': 2, 'ensure_ascii': False},
    )
