# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Development'
        db.create_table(u'webapp_development', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('mobile', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('project_budget', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('project_start_date', self.gf('django.db.models.fields.DateField')()),
            ('project_file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('project_message', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('created', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('update', self.gf('django.db.models.fields.DateField')(auto_now=True, auto_now_add=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'webapp', ['Development'])


    def backwards(self, orm):
        # Deleting model 'Development'
        db.delete_table(u'webapp_development')


    models = {
        u'webapp.development': {
            'Meta': {'object_name': 'Development'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'project_budget': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'project_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'project_message': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'project_start_date': ('django.db.models.fields.DateField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'update': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['webapp']