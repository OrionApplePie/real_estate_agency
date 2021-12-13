from django.contrib import admin

from .models import Flat, Complaint, Owner

class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'owner', 'address',)
    readonly_fields = ('created_at',)
    raw_id_fields = ('liked_by',)

    list_editable = ('new_building',)
    list_display = (
        'address',
        'owners_phonenumber',
        'owners_pure_phone',
        'price',
        'new_building',
        'construction_year',
        'town',
    )
    list_filter = (
        'new_building',
        'rooms_number',
        'has_balcony',
    )


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)

    search_fields = (
        'full_name',
        'phonenumber',
        'pure_phone',
    )


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
