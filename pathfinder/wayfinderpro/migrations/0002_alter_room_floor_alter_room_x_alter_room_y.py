# Generated by Django 5.0.4 on 2024-05-02 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wayfinderpro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='floor',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='room',
            name='x',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='room',
            name='y',
            field=models.IntegerField(),
        ),
    ]
