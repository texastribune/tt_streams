import datetime

from django.utils import timezone
import factory

from . import models


class StreamFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = models.Stream


class NodeFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = models.Node

    pub_date = factory.LazyAttribute(lambda a: timezone.now())
