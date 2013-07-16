from tt_streams.models import Stream, StreamItem
from django.db import models


class StoryItem(StreamItem):
    story = models.ForeignKey('Story')


class Story(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    stream = models.ManyToManyField(Stream, through=StoryItem)

    def __unicode__(self):
        return self.title


class VideoItem(StreamItem):
    video = models.ForeignKey('Video')


class Video(models.Model):
    title = models.CharField(max_length=250)
    url = models.URLField()
    stream = models.ManyToManyField(Stream, through=VideoItem)

    def __unicode__(self):
        return self.title
