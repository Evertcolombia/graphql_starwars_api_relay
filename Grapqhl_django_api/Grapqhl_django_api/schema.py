import graphene

import Grapqhl_django_api.api_project.schema

class Query(Grapqhl_django_api.api_project.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Mutation(Grapqhl_django_api.api_project.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)