from django.db import models

# Create your models here.

#from django.db import models

class Planet(models.Model):
    """ Planet Model Entity

        Create a Model object for the each Planet

    Returns:
        [string]: name of the new planet
    """    
    name = models.CharField(max_length=100)
    surface_water = models.CharField(max_length=40)
    diameter = models.CharField(max_length=40)
    climate = models.CharField(max_length=40)
    gravity = models.CharField(max_length=40)
    terrain = models.CharField(max_length=40)
    population = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Film(models.Model):
    """Film Model Entity

        Create a Model object for the each Film in the saga

    Returns:
        [string]: name of the Film
    """    
    title = models.CharField(max_length=100)
    episode_id = models.IntegerField()
    opening_crawl = models.TextField(max_length=1000)
    director = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    release_date = models.DateField()
    planets = models.ManyToManyField(
        Planet,
        related_name="films",
        blank=True
    )    
    def __str__(self):
        return self.title


class People(models.Model):
    """People Model Entity

        Create a Model object for the each People in the saga for a movie

    Returns:
        [string]: name of the People
    """    
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=40, blank=True)
    skin_color = models.CharField(max_length=20, blank=True)
    height = models.CharField(max_length=10, blank=True)
    eye_color = models.CharField(max_length=20, blank=True)
    films = models.ManyToManyField(
        Film,
        related_name="characters",
        blank=True    
    )
    def __str__(self):
        return self.name

