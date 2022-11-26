from datetime import datetime

from django.test import TestCase

from ...models import Identity
from ..factories import PersonFactory


class PersonTestCase(TestCase):
    def test_attributes(self):
        person = PersonFactory.create(name="John Doe")
        assert person.name == "John Doe"
        assert type(person.identity) == Identity
        assert type(person.created_at) == datetime
        assert person.updated_at.date() == person.created_at.date()

        person.save()
        assert person.updated_at > person.created_at
