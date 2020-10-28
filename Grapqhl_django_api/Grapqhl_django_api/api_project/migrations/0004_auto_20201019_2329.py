# Generated by Django 3.1.2 on 2020-10-19 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_project', '0003_auto_20201019_2212'),
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('episode_id', models.IntegerField()),
                ('openin_crawl', models.TextField(max_length=1000)),
                ('director', models.CharField(max_length=100)),
                ('producer', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Pokemon',
        ),
        migrations.DeleteModel(
            name='Type',
        ),
    ]