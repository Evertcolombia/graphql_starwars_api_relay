from graphene import Schema, ObjectType, Field, List, String, Node, Connection, Int, relay, ID, Mutation
from graphene_django import DjangoObjectType

from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.debug import DjangoDebug

from .models import Film, People, Planet
from .nodes import FilmType, PeopleType, PlanetType
from graphql_relay import from_global_id

import graphql_jwt


def resolve_user(info):
    """ Resolver user authentication for each query where If function
    will be called

    Args:
        info ([objec]): Info about user and context session

    Raises:
        Exception: User is not logged on admin page
    """    
    user = info.context.user
    if not user.is_authenticated:
        msg = "Admin Credential where not provided. Please do login at http://localhost:8000/admin"
        raise Exception(msg) 


# Connection Node Classes
class PlanetConnection(relay.Connection):
    """ Create a Connection edge of the PlanetType Node

    Args:
        relay ([objec]): [makes possible the connection]
    """    
    class Meta:
        node = PlanetType

class PeopleConnection(relay.Connection):
    """ Create a Connection edge of the PeopleType Node

    Args:
        relay ([objec]): [makes possible the connection]
    """
    class Meta:
        node = PeopleType

class FilmConnection(relay.Connection):
    """ Create a Connection edge of the FilmType Node

    Args:
        relay ([objec]): [makes possible the connection]
    """
    class Meta:
        node = FilmType
        

# Mutation Classes

"""  IT DOES NOT WORK 

class FilmCreateMutation(relay.ClientIDMutation):
    class Input:
        title: String()
    
    film = Field(FilmType)

    
    def mutate_and_get_payload(cls, root, info, title):
        film = FilmType(title=title)
        film.save()
        return FilmCreateMutation(film=film)
"""

class FilmUpdateMutation(relay.ClientIDMutation):
    """ Update Mutation For FilmType nodes can update any objec of this type

    Args:
        relay ([object]): [Use clien mutation id to get to use globals id that relay give to us]

    Returns:
        [FilmType]: [Updated Film on success]
    """    
    class Input:
        """[pass input fiel that can be changed ]
        """        
        title = String()
        director = String()
        producer = String()
        planets = List(String)
        opening_crawl = String()
        id = ID(required=True)
    
    film = Field(FilmType)

    @classmethod
    
    def mutate_and_get_payload(cls, root, info, id,
                                title, director, producer, opening_crawl): #planets
        """[Make the mutation and get back the payload object]

        Args:
            info ([object]): [session context contain]
            id ([ID]): [Global id for the film]
            title ([string]): [title of the movie]
            director ([string]): [director of the movie]
            producer ([string]): [producer of the movie]
            opening_crawl ([string]): [oening crawl of the movie]

        Returns:
            [FilmType]: [updated filmtype object]
        """        
        resolve_user(info)
        film = Film.objects.get(id=from_global_id(id)[1])
        if title is not None:
            film.title = title
        if director  is not None:
            film.director = director
        if producer is not None:
            film.producer = producer # [film.producer.append(p) for p in producer if p not in film.producer]
        if opening_crawl is not None:
            film.opening_crawl = opening_crawl 
        #if planets is not None:
            #film.planets = planets # [film.planets.append(f) for f in planets if f not in film.planets]
        film.save()

        return FilmUpdateMutation(film=film)


class PlanetUpdateMutation(relay.ClientIDMutation):    
    class Input:
        """[pass input fiel that can be changed ]
        """ 
        name = String()
        climate = String()
        terrain = String()
        population = String()
        id = ID(required=True)
    
    planet = Field(PlanetType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, id, name,
                                climate, terrain, population):
        """[Make the mutation and get back the payload object]

        Args:
            info ([object]): [session context contain]
            id ([ID]): [Global id for the planet]
            name ([string]): [name of the planet]
            terrain ([string]): [terrain class of the planet]
            population ([string]): [population total in the olanet]

        Returns:
            [PlanetType]: [updated PlanetType object]
        """
        resolve_user(info)
        planet = Planet.objects.get(id=from_global_id(id)[1])
        if name is not None:
            planet.name = name
        if climate  is not None:
            planet.climate = climate
        if terrain is not None:
            planet.terrain = terrain
        if population is not None:
            planet.population = population
        planet.save()

        return PlanetUpdateMutation(planet=planet)


class PeopleUpdateMutation(relay.ClientIDMutation):
    """ Update Mutation For PeopleType nodes can update any objec of this type

    Args:
        relay ([object]): [Use clien mutation id to get to use globals id that relay give to us]

    Returns:
        [PeopleType]: [Updated People on success]
    """
    class Input:
        """[pass input fiel that can be changed ]
        """
        name = String()
        gender = String()
        skin_color = String()
        height = String()
        eye_color = String()
        films = List(String)
        id = ID(required=True)
    
    people = Field(PeopleType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, id, name,
                                gender, skin_color, height, eye_color): # films
        
        """[Make the mutation and get back the payload object]

        Args:
            info ([object]): [session context contain]
            id ([ID]): [Global id for the People]
            gender ([string]): [gender of the People]
            skin_color ([string]): [skin_color class of the People]
            height ([string]): [height total in the people]
            eye_color ([string]): [eye color of the people]

        Returns:
            [PeopleType]: [updated PeopleType object]
        """
        resolve_user(info)   
        people = People.objects.get(id=from_global_id(id)[1])
        if name is not None:
            people.name = name
        if gender  is not None:
            people.gender = gender
        if skin_color is not None:
            people.skin_color = skin_color
        if height is not None:
            people.height = height
        if eye_color is not None:
            people.eye_color = eye_color
        #if films is not None:
            #people.films = films
            # people.films = [people.films.append(f) for f in films if f not in people.films]
        people.save()

        return PeopleUpdateMutation(people=people)


# QUERY and MUTATION class
class Query(ObjectType):
    """ QUery Class that recives querys likes api calls

    Args:
        ObjectType (graphene): [idetifed the odbject node for the call]
    """    
    one_film = relay.Node.Field(FilmType)
    specific_movie = DjangoFilterConnectionField(FilmType)
    all_films = relay.ConnectionField(FilmConnection)

    one_person = relay.Node.Field(PeopleType)
    specific_person = DjangoFilterConnectionField(PeopleType)
    all_person = relay.ConnectionField(PeopleConnection)

    one_planet = relay.Node.Field(PlanetType)
    specific_planet =  DjangoFilterConnectionField(PlanetType)
    all_planet = relay.ConnectionField(PlanetConnection)

    def resolve_all_films(root, info, **kwargs):
        resolve_user(info)
        return  Film.objects.all()
    
    def resolve_all_person(root, info, **kwargs):
        resolve_user(info)
        return People.objects.all()

    def resolve_all_planet(root, info, **kwargs):
        resolve_user(info)
        return Planet.objects.all()

    debug = Field(DjangoDebug, name='__debug')


class Mutation:
    """ Mutaiton Class that recives querys  likes api calls for updates and otherss
    """
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()

    #create_film = FilmCreateMutation.Field()
    update_film = FilmUpdateMutation.Field()
    update_planet = PlanetUpdateMutation.Field()
    update_people = PeopleUpdateMutation.Field()


schema = Schema(Query)
result = schema.execute(
    '''
    query person($name: String) {
        specificPerson(name: $name) {
            edges {
                node {
                    id
                    name
                    gender
                    skinColor
                    height
                    eyeColor
                    films {
                        edges {
                            node {
                                id
                                title
                                director producer
                                planets {
                                    edges {
                                        node {
                                            name 
                                            population
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            } 
        }
    }
    ''',
    variables={'name': put_the_name}
)