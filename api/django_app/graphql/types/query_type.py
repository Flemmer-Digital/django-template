import graphene

from .person_type import PersonType


class Query(graphene.ObjectType):
    current_person = graphene.Field(PersonType)

    def resolve_current_person(root, info, **kargs):
        return info.context.user.person
