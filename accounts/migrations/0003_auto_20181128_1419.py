# Generated by Django 2.0.8 on 2018-11-28 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_artist_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='Bio',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
