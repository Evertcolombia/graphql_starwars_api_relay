# Generated by Django 3.1.2 on 2020-10-25 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_project', '0010_delete_people'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('height', models.CharField(blank=True, max_length=10)),
                ('mass', models.CharField(blank=True, max_length=10)),
                ('hair_color', models.CharField(blank=True, max_length=20)),
                ('skin_color', models.CharField(blank=True, max_length=20)),
                ('eye_color', models.CharField(blank=True, max_length=20)),
                ('birth_year', models.CharField(blank=True, max_length=10)),
                ('gender', models.CharField(blank=True, max_length=40)),
            ],
        ),
    ]
