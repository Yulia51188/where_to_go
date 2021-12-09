from django.shortcuts import render
from places.models import Place


def serialize_place(place):
    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [place.longitude, place.latitude],
        },
        "properties": {
            "title": place.place_id,
            "placeId": place.place_id,
            "detailsUrl": place.details.url,
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
