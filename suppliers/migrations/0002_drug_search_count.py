# Generated by Django 5.1.1 on 2024-10-01 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='search_count',
            field=models.IntegerField(default=0),
        ),
    ]
