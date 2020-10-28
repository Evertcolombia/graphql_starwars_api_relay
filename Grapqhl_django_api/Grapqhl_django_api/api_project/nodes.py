from graphene import relay
from graphene_django import DjangoObjectType

from .models import Film, People, Planet


class FilmType(DjangoObjectType):
    """ Node of type Film for each  Film 

    Args:
        DjangoObjectType: Create an object identified as DjangoObjectType classs
    """    
    class Meta:
        model = Film
        filter_fields = ['title']
        interfaces = (relay.Node,)


class PlanetType(DjangoObjectType):
    """ Node of type Planet for each  Planet 

    Args:
        DjangoObjectType: Create an object identified as DjangoObjectType classs
    """     
    class Meta: 
        model = Planet
        #exclude_fields = ('climate', 'terrain')
        filter_fields = { 
            'name': ['exact']
        }
        interfaces = (relay.Node,)
    

class PeopleType(DjangoObjectType):
    """ Node of type People for each  People 

    Args:
        DjangoObjectType: Create an object identified as DjangoObjectType classs
    """    
    class Meta:
        model = People
        filter_fields = { 
            'name': ['exact']
        }
        interfaces = (relay.Node,)