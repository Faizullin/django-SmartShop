import factory
from django.contrib.auth.models import User, Group
from django.utils import timezone
from .models import Shop,ShopData,Good,GoodType

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@example.com")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    is_staff = False
    is_active = True
    date_joined = factory.LazyFunction(timezone.now)


class SuperuserFactory(UserFactory):
    is_staff = True
    is_superuser = True


class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Group

    name = factory.Sequence(lambda n: f"group{n}")


class GoodTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GoodType