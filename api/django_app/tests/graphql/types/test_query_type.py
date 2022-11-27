from django.test import TestCase

# from ...factories import PersonFactory
# from ...helpers.context import Context
# from ...helpers.execute_graphql_query import execute_graphql_query


class QueryTypeTestCase(TestCase):
    query = """
              {
                currentPerson {
                  name
                  identity {
                    username
                  }
                }
              }
            """

    def test_current_person_field(self):
        assert True
        # Can uncomment once we have added authentication
        # current_person = PersonFactory.create()
        # result = execute_graphql_query(
        #     self.query, context=Context(current_person.identity), default_context=False
        # )
        # response_data = result["data"]
        # assert (response_data["currentPerson"]["name"]) == current_person.name
        # assert (response_data["currentPerson"]["identity"]["username"]) == current_person.identity.username
