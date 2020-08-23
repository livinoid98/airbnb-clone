from django.contrib import admin
from django.utils.html import mark_safe
from .import models

@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "used_by"
    )

    def used_by(self,obj):
        return obj.rooms.count()

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    fieldsets = (
        (
            "Basic Info",
            {
                "fields":("name","description","country","address","price")
            }
        ),
        (
            "Times",
            {
                "fields":("check_in","check_out","instant_book")
            }
        ),
        (
            "Spaces",
            {
                "fields":("guests","beds","bedrooms","baths")
            }
        ),
        (
            "More About the Space",
            {
                "classes":("collapse",),
                "fields":("amenities","facilities","house_rules")
            }
        ),
        (
            "Last Details", 
            {
                "fields":("host",)
            }
        ),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "host__gender",
        "room_type",
        "amenities",
        "facilities",
        "house_rule",
        "city",
        "country",
    )

    ordering = ("name", "price", "bedrooms")

    search_fields = (
        "=city",
        "^host__username",
    )

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rule",
    )

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def count_amenities(self, obj):
        return obj.amenities.count()

    count_amenities.short_description = "hello"

    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    list_display = ('__str__', 'get_thumbnail')

    def get_thumbnail(self, obj):
        return mark_safe(f'<img src="{obj.file.url}"/>')

    get_thumbnail.short_description = "Thumbnail"
