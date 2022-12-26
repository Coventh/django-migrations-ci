# Generated by Django 4.1.2 on 2022-10-20 18:43

from django.db import migrations


def create_one_bus(apps, schema_editor):
    Bus = apps.get_model("testapp", "Bus")
    Bus.objects.create(plate="BUS3R")


class Migration(migrations.Migration):
    dependencies = [
        ("testapp", "0001_initial"),
    ]

    operations = [migrations.RunPython(create_one_bus, migrations.RunPython.noop)]
