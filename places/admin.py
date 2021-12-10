from django.contrib import admin
from places.models import Place, PlacePhoto
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableInlineAdminMixin


class PlacePhotoInline(SortableInlineAdminMixin, admin.TabularInline):
    extra = 1

    model = PlacePhoto
    readonly_fields = ['image_preview']
    fields = ('image', 'image_preview', 'index')

    def image_preview(self, obj, max_height=200):
        preview_template = '<img src="{url}" height="{height}" width="{width}"/>'
        width = obj.image.width * max_height / obj.image.height
        return mark_safe(preview_template.format(
            url=obj.image.url,
            height=max_height,
            width=width,
        ))


class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        PlacePhotoInline,
    ]


admin.site.register(Place, PlaceAdmin)
admin.site.register(PlacePhoto)
