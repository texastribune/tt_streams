from django.db import models
from model_utils.managers import InheritanceManager


class Stream(models.Model):
    slug = models.SlugField()

    def __unicode__(self):
        return self.slug


class Node(models.Model):
    stream = models.ForeignKey(Stream, related_name='nodes')
    pub_date = models.DateTimeField()

    objects = InheritanceManager()
