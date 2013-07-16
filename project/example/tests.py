from functools import wraps

from django.test import TestCase

from tt_streams import factories as streams

from . import factories
from . import models


def with_stream_stories_and_videos(func):
    @wraps(func)
    def inner(self, *args, **kwargs):
        stream = streams.StreamFactory.create()
        stories = [factories.StoryFactory.create() for a in range(2)]
        for s in stories:
            factories.StoryItemFactory.create(stream=stream, story=s)
        videos = [factories.VideoFactory.create() for a in range(2)]
        for v in videos:
            factories.VideoItemFactory.create(stream=stream, video=v)
        return func(self, stream, stories, videos, *args, **kwargs)
    return inner


class BasicUsageTestCase(TestCase):
    def test_can_find_stories_in_stream(self):
        stream = streams.StreamFactory.create()
        stories = [factories.StoryFactory.create() for a in range(2)]
        for s in stories:
            factories.StoryItemFactory.create(stream=stream, story=s)

        self.assertEqual(stream.items.count(), 2)

    def test_can_find_videos_in_stream(self):
        stream = streams.StreamFactory.create()
        videos = [factories.VideoFactory.create() for a in range(2)]
        for v in videos:
            factories.VideoItemFactory.create(stream=stream, video=v)

        self.assertEqual(stream.items.count(), 2)

    @with_stream_stories_and_videos
    def test_can_find_both_videos_and_stories(self, stream, stories, videos):
        self.assertEqual(stream.items.count(), 4)

    @with_stream_stories_and_videos
    def test_returns_full_classes(self, stream, stories, videos):
        for s in models.StoryItem.objects.all():
            self.assert_(s in stream.items.select_subclasses().all())

        for v in models.VideoItem.objects.all():
            self.assert_(v in stream.items.select_subclasses().all())
