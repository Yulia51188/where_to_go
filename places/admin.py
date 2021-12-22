from django.contrib import admin
from places.models import Place, PlacePhoto
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin


class PlacePhotoInline(SortableInlineAdminMixin, admin.TabularInline):
    extra = 1

    model = PlacePhoto
    readonly_fields = ['image_preview']
    fields = ('image', 'image_preview', 'index')

    def image_preview(self, obj, max_height=200):
        preview_template = '<img src="{}" height="{}" width="{}"/>'
        width = obj.image.width * max_height / obj.image.height
        return format_html(
            preview_template,
            mark_safe(obj.image.url),
            mark_safe(max_height),
            mark_safe(width),
        )


class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        PlacePhotoInline,
    ]
    search_fields = ['title']
    list_display = ['title', 'slug']


admin.site.register(Place, PlaceAdmin)
admin.site.register(PlacePhoto)
