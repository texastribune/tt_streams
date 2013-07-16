from tt_streams.models import Stream, StreamItem
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class StoryItem(StreamItem):
    story = models.ForeignKey('Story', related_name='stream_items')
    title = models.CharField(max_length=250)

    def save(self, *args, **kwargs):
        self.title = self.story.title
        return super(StoryItem, self).save(*args, **kwargs)


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


@receiver(post_save, sender=Story)
def update_story_item(sender, instance=None, **kwargs):
    for item in instance.stream_items.all():
        item.save()
