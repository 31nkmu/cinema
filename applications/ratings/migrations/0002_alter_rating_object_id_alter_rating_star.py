# Generated by Django 4.1.4 on 2022-12-10 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='object_id',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='rating',
            name='star',
            field=models.PositiveSmallIntegerField(choices=[(1, '1/5')]),
        ),
    ]
