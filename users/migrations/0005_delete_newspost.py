# Generated by Django 4.2 on 2023-05-05 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_newspost_slug_alter_newspost_author_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NewsPost',
        ),
    ]
