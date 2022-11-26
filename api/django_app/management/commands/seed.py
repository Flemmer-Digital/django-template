from django.core.management.base import BaseCommand

from api.django_app.tests.factories import IdentityFactory


def create_super_user():
    return IdentityFactory.create(
        username="staff@django.com",
        email="staff@django.com",
        is_staff=True,
        is_superuser=True,
    )


class Command(BaseCommand):
    help = "Seeds the database"

    def handle(self, *args, **options):
        create_super_user()
        print("Database seeded")
