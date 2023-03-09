from django.contrib.auth.models import Group
from .factories import *


def seed():
    groupOwner = GroupFactory.create(name="groupOwner")

    # Create superusers
    superuser1 = SuperuserFactory.create(
        name="admin",
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
    # for _ in range(10):
    #     user = UserFactory.create()

    print("Seed complete!")
