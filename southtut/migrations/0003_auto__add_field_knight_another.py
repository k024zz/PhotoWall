# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Knight.another'
        db.add_column(u'southtut_knight', 'another',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Knight.another'
        db.delete_column(u'southtut_knight', 'another')


    models = {
        u'southtut.knight': {
            'Meta': {'object_name': 'Knight'},
            'another': ('django.db.models.fields.BooleanField', [], {}),
            'dances_whenever_able': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'of_the_round_table': ('django.db.models.fields.BooleanField', [], {})
        }
    }

    complete_apps = ['southtut']