import factory
from faker import Factory as FakerFactory

from Apres_Ski_API.models.comment import Comment
from Apres_Ski_API.models.engagement import Engagement
from Apres_Ski_API.models.happyhour import HappyHour
from Apres_Ski_API.models.hour import Hour
from Apres_Ski_API.models.lift import Lift
from Apres_Ski_API.models.photo import Photo
from Apres_Ski_API.models.restaurant import Restaurant
from Apres_Ski_API.models.user import User

faker = FakerFactory.create()

class UserFactory(factory.django.DjangoModelFactory):
    name = factory.LazyAttribute(lambda x: faker.name())
    lat = factory.LazyAttribute(lambda x: faker.aba())
    lon = factory.LazyAttribute(lambda x: faker.aba())

    class Meta:
        model = User

class RestaurantFactory(factory.django.DjangoModelFactory):
    name = factory.LazyAttribute(lambda x: faker.name())
    address = factory.LazyAttribute(lambda x: faker.address())
    food_type = factory.LazyAttribute(lambda x: faker.name())
    cost = factory.LazyAttribute(lambda x: faker.pricetag())
    cover_img = factory.LazyAttribute(lambda x: faker.name())
    alt_text = factory.LazyAttribute(lambda x: faker.name())
    lat = factory.LazyAttribute(lambda x: faker.aba())
    lon = factory.LazyAttribute(lambda x: faker.aba())
    alcoholic_drinks = factory.LazyAttribute(lambda x: faker.boolean(chance_of_getting_true=25))
    has_happy_hour = factory.LazyAttribute(lambda x: faker.boolean(chance_of_getting_true=25))

    class Meta:
        model = Restaurant

class LiftFactory(factory.django.DjangoModelFactory):
    name = factory.LazyAttribute(lambda x: faker.name())
    lat = factory.LazyAttribute(lambda x: faker.aba())
    lon = factory.LazyAttribute(lambda x: faker.aba())

    class Meta:
        model = Lift

class HourFactory(factory.django.DjangoModelFactory):
    sunday = factory.LazyAttribute(lambda x: faker.aba())
    monday = factory.LazyAttribute(lambda x: faker.aba())
    tuesday = factory.LazyAttribute(lambda x: faker.aba())
    wednesday = factory.LazyAttribute(lambda x: faker.aba())
    thursday = factory.LazyAttribute(lambda x: faker.aba())
    friday = factory.LazyAttribute(lambda x: faker.aba())
    saturday = factory.LazyAttribute(lambda x: faker.aba())
    restaurant = factory.SubFactory(RestaurantFactory)

    class Meta:
        model = Hour

class HappyHourFactory(factory.django.DjangoModelFactory):
    sunday = factory.LazyAttribute(lambda x: faker.aba())
    monday = factory.LazyAttribute(lambda x: faker.aba())
    tuesday = factory.LazyAttribute(lambda x: faker.aba())
    wednesday = factory.LazyAttribute(lambda x: faker.aba())
    thursday = factory.LazyAttribute(lambda x: faker.aba())
    friday = factory.LazyAttribute(lambda x: faker.aba())
    saturday = factory.LazyAttribute(lambda x: faker.aba())
    special = factory.LazyAttribute(lambda x: faker.aba())
    restaurant = factory.SubFactory(RestaurantFactory)

    class Meta:
        model = HappyHour

class PhotoFactory(factory.django.DjangoModelFactory):
    url = factory.LazyAttribute(lambda x: faker.aba())
    alt_text= factory.LazyAttribute(lambda x: faker.aba())
    restaurant = factory.SubFactory(RestaurantFactory)

    class Meta:
        model = Photo

class CommentFactory(factory.django.DjangoModelFactory):
    comment = factory.LazyAttribute(lambda x: faker.aba())
    restaurant = factory.SubFactory(RestaurantFactory)
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Comment

class EngagementFactory(factory.django.DjangoModelFactory):
    vibe = factory.LazyAttribute(lambda x: faker.aba())
    rating = factory.LazyAttribute(lambda x: faker.aba())
    favorites = factory.LazyAttribute(lambda x: faker.boolean(chance_of_getting_true=25))
    restaurant = factory.SubFactory(RestaurantFactory)
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Engagement
