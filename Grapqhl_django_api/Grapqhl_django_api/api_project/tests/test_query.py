import json
from graphene_django.utils.testing import GraphQLTestCase


class MyFancyTestCase(GraphQLTestCase):
     def test_query_with_variables(self):
        response = self.query(
            '''
            query oneFilm($id: Int!){
                oneFilm(id: $id) {
                    id
                    title
                    director
                    producer
                }
            }
            ''',
            op_name='myModel',
            variables={'id': ""}
        )

        content = json.loads(response.content)

        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)

        print(content)
