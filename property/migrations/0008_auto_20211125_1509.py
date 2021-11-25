# Generated by Django 2.2.24 on 2021-11-25 05:09

import phonenumbers as pn
from django.db import migrations
from phonenumbers import NumberParseException


def normalize_phonenumber(apps, schema_editor):
    try:
        Flat = apps.get_model('property', 'Flat')
    except LookupError:
        return None

    for flat in Flat.objects.all():
        raw_phonenumber = flat.owners_phonenumber
        try:
            parsed_phonenumber = pn.parse(raw_phonenumber, 'RU')
        except NumberParseException:
            continue

        if (pn.is_valid_number(parsed_phonenumber)
            and pn.is_possible_number(parsed_phonenumber)
        ):
            flat.owners_pure_phone = parsed_phonenumber
            flat.save()


def move_backward(apps, schema_editor):
    try:
        Flat = apps.get_model('property', 'Flat')
    except LookupError:
        return None

    for flat in Flat.objects.all():
        flat.owners_pure_phone = None
        flat.save()

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_owners_pure_phone'),
    ]

    operations = [
        migrations.RunPython(normalize_phonenumber, move_backward)
    ]
