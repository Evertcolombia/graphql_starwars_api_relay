# Generated by Django 3.1.2 on 2020-10-25 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_project', '0014_auto_20201025_2123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rotation_period', models.CharField(max_length=40)),
                ('orbital_period', models.CharField(max_length=40)),
                ('diameter', models.CharField(max_length=40)),
                ('climate', models.CharField(max_length=40)),
                ('gravity', models.CharField(max_length=40)),
                ('terrain', models.CharField(max_length=40)),
                ('surface_water', models.CharField(max_length=40)),
                ('population', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='planets',
            field=models.ManyToManyField(blank=True, related_name='films', to='api_project.Planet'),
        ),
    ]
