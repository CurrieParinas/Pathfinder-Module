# Generated by Django 4.2.7 on 2024-05-18 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wayfinderpro', '0003_remove_room_floor_room_floornumber_room_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='floorNumber',
            field=models.IntegerField(default=1),
        ),
    ]
