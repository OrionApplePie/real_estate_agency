# Generated by Django 2.2.24 on 2021-12-13 02:22

from django.db import migrations


def link_owner_flat(apps, schema_editor):
    try:
        Flat = apps.get_model('property', 'Flat')
        Owner = apps.get_model('property', 'Owner')
    except LookupError:
        return None

    for flat in Flat.objects.all():
        owner, _ = Owner.objects.get_or_create(
            full_name=flat.owner,
            phonenumber=flat.owners_phonenumber,
            defaults={
                'pure_phone': flat.owners_pure_phone,
            }
        )
        owner.flats.add(flat)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20211213_1212'),
    ]

    operations = [
        migrations.RunPython(link_owner_flat)
    ]