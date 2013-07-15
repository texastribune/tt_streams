from tt_streams.models import Node, Stream
from django.db import models


class StoryNode(Node):
    story = models.ForeignKey('Story')


class Story(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    stream = models.ManyToManyField(Stream, through=StoryNode)

    def __unicode__(self):
        return self.title


class VideoNode(Node):
    video = models.ForeignKey('Video')


class Video(models.Model):
    title = models.CharField(max_length=250)
    url = models.URLField()
    stream = models.ManyToManyField(Stream, through=VideoNode)

    def __unicode__(self):
        return self.title
