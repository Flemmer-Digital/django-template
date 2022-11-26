from graphene_django import DjangoObjectType

from ...models.person import Person


class PersonType(DjangoObjectType):
    class Meta:
        model = Person
        fields = "__all__"
