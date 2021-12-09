from django.contrib import admin
from places.models import Place, PlacePhoto


class PlacePhotoInline(admin.TabularInline):
    model = PlacePhoto


class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        PlacePhotoInline,
    ]


admin.site.register(Place, PlaceAdmin)
admin.site.register(PlacePhoto)