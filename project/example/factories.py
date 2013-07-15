import factory

from tt_streams import factories

from . import models


class StoryFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = models.Story


class StoryNodeFactory(factories.NodeFactory):
    FACTORY_FOR = models.StoryNode


class VideoFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = models.Video


class VideoNodeFactory(factories.NodeFactory):
    FACTORY_FOR = models.VideoNode
