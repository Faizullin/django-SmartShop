from django.contrib.auth.models import Group
from .factories import *
from django.db import transaction

#@transaction.atomic
def seed():
    
    try:
        with transaction.atomic():
            groupOwner = GroupFactory.create(name="groupOwner")

            # Create superusers
            superuser1 = SuperuserFactory.create(
                username="admin",
                email="admin@example.com",
                password="password",
            )
            superuser1.groups.set([groupOwner])

            for _ in range(5):
                user = UserFactory.create(
                    password="password"
                )
                user.groups.set([groupOwner])
            for _ in range(10):
                user = UserFactory.create(
                    password="password"
                )

            GoodTypeFactory.create(name='vegetables')
            for _ in range(10):
                 GoodFactory.create()
            for _ in range(5):
                shopData = ShopDataFactory.create()
                ShopFactory.create(
                    data = shopData,
                )

        print('Data seeded successfully.')
    except Exception as e:
        print('Error seeding data:', str(e))
        raise e
