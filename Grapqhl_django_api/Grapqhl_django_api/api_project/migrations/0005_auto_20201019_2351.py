# Generated by Django 3.1.2 on 2020-10-19 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_project', '0004_auto_20201019_2329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='openin_crawl',
            new_name='opening_crawl',
        ),
    ]
