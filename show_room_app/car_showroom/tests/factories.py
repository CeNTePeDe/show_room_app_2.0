import random
from decimal import Decimal

import factory
from factory import fuzzy

from car_showroom.models import CarShowRoom, SellModel
from faker import Faker

from cars.choice import Color, EnginType, NumberOfDoor, BodyType
from cars.tests.factories import CarFactory
from core.tests.factories import JSONFactory
from discount.tests.factories import ProviderDiscountFactory, SeasonDiscountFactory
from provider.tests.factories import ProviderFactory
from user.tests.factories import UserFactory

faker = Faker()


class CarShowRoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CarShowRoom

    name = faker.name()
    year = int(faker.year())
    balance = Decimal("23.99")
    country = random.choice(["CA", "FR", "DE", "IT", "JP", "RU", "GB"])
    characteristic = factory.Dict(
        {
            "color": fuzzy.FuzzyChoice(Color),
            "engine_type": fuzzy.FuzzyChoice(EnginType),
            "number_of_doors": fuzzy.FuzzyChoice(NumberOfDoor),
            "body_type": fuzzy.FuzzyChoice(BodyType),
        },
        dict_factory=JSONFactory,
    )

    is_active = True
    user = factory.SubFactory(UserFactory)


class SellModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SellModel

    car = factory.SubFactory(CarFactory)
    car_showroom = factory.SubFactory(CarShowRoomFactory)
    provider = factory.SubFactory(ProviderFactory)
    discount = factory.SubFactory(ProviderDiscountFactory)
    season_discount = factory.SubFactory(SeasonDiscountFactory)
    margin = random.randint(0, 100)
    number_of_cars = random.randint(0, 100)


class CarShowRoomWithSellFactory(CarShowRoomFactory):
    Sell = factory.RelatedFactory(SellModelFactory, factory_related_name="sell")