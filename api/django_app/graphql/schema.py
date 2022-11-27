import graphene

from .types.query_type import Query

schema = graphene.Schema(query=Query)
