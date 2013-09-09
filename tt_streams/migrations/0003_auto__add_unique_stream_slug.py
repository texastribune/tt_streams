# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Stream', fields ['slug']
        db.create_unique(u'tt_streams_stream', ['slug'])


    def backwards(self, orm):
        # Removing unique constraint on 'Stream', fields ['slug']
        db.delete_unique(u'tt_streams_stream', ['slug'])


    models = {
        u'tt_streams.stream': {
            'Meta': {'object_name': 'Stream'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'summary': ('django.db.models.fields.TextField', [], {})
        },
        u'tt_streams.streamitem': {
            'Meta': {'object_name': 'StreamItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'stream': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': u"orm['tt_streams.Stream']"})
        }
    }

    complete_apps = ['tt_streams']