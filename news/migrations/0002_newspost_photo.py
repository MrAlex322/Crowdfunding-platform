# Generated by Django 4.2 on 2023-05-10 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspost',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='news_photos/'),
        ),
    ]
