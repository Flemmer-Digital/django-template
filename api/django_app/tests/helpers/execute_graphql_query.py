from django.urls import reverse
from graphene.test import Client
from rest_framework.test import APIClient

from api.django_app.graphql.schema import schema

from ..factories.identity_factory import IdentityFactory
from .context import Context


def execute_graphql_query(
    api_query,
    context,
    default_context=True,
    variable_values=None,
    authenticated=True,
    **kwargs
):
    if default_context:
        if bool(context):
            raise Exception(
                "Context provided and default context also being used,"
                "either remove the context or set default_context=False"
            )
        context = get_default_context()

    if authenticated:
        login(context.user)

    graphql_client = Client(schema)
    result = graphql_client.execute(
        api_query, variable_values=variable_values, context=context, **kwargs
    )
    return result


def login(identity):
    rest_client = APIClient()
    rest_client.post(
        reverse("rest_login"),
        {"username": identity.username, "password": "password"},
        format="json",
    )


def get_default_context():
    identity = IdentityFactory.create(username="identity_username", password="password")
    return Context(identity)
