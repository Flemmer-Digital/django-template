import factory

from api.django_app.models import Identity

from .person_factory import PersonFactory


class IdentityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Identity

    is_staff = False
    is_superuser = False
    is_active = True

    email = factory.Faker("email")
    username = factory.Faker("user_name")
    password = factory.PostGenerationMethodCall("set_password", "password")

    person = factory.RelatedFactory(PersonFactory, factory_related_name="identity")
