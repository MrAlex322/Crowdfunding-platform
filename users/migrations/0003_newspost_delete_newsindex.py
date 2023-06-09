# Generated by Django 4.2 on 2023-04-27 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_newsindex'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=10)),
                ('number_of_views', models.IntegerField(blank=True, null=True)),
                ('body', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='NewsIndex',
        ),
    ]
