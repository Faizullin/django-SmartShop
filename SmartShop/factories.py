import factory, random
from django.contrib.auth.models import User, Group
from django.utils import timezone
from .models import Shop, ShopData, Good, GoodType, Purchase

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
    password = factory.PostGenerationMethodCall('set_password',
                                                'defaultpassword')


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



class ShopDataFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ShopData
    name = factory.Faker("first_name")
    owner = factory.SubFactory(UserFactory)
    open = bool(random.randint(0,1))
    street = factory.Faker("address")
    city = factory.Faker("city")
    state = factory.Faker("address")
    zip_code = "010000"
    


class ShopFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Shop
    name = factory.Faker("first_name")
    owner = factory.SubFactory(UserFactory)
    data=factory.SubFactory(ShopDataFactory)

class GoodFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Good
    name = factory.Faker("first_name")
    description = factory.Faker("sentence")
    price = random.randint(2,10)
    type = factory.SubFactory(GoodTypeFactory)
    shop = factory.SubFactory(ShopFactory)

class PurchaseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Purchase
    user = factory.SubFactory(UserFactory)
    shop = factory.SubFactory(ShopFactory)
    goods = factory.SubFactory(GoodFactory)
    quantity = random.randint(0,10)
    total_price = 0
    is_completed = bool(random.randint(0,1))