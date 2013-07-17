import factory

from tt_streams import factories

from . import models


class StoryFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = models.Story


class StoryItemFactory(factories.StreamItemFactory):
    FACTORY_FOR = models.StoryItem


class VideoFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = models.Video


class VideoItemFactory(factories.StreamItemFactory):
    FACTORY_FOR = models.VideoItem
