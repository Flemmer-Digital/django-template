import factory

from api.django_app.models import Person


class PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Person

    name = factory.Faker("name")
    identity = factory.SubFactory(
        "api.django_app.tests.factories.IdentityFactory", person=None
    )
