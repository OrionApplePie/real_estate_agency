from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Flat.owners.through

    raw_id_fields = ('owner', 'flat',)


@admin.register(Flat)
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

    inlines = [
        OwnerInline,
    ]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)

    search_fields = (
        'full_name',
        'phonenumber',
        'pure_phone',
    )
