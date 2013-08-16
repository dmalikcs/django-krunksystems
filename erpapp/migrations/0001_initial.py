# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ERPInquiry'
        db.create_table(u'erpapp_erpinquiry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('job_title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('company_name', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('company_website', self.gf('django.db.models.fields.URLField')(max_length=75)),
            ('product', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('message', self.gf('django.db.models.fields.TextField')(max_length=200)),
            ('created', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('update', self.gf('django.db.models.fields.DateField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'erpapp', ['ERPInquiry'])


    def backwards(self, orm):
        # Deleting model 'ERPInquiry'
        db.delete_table(u'erpapp_erpinquiry')


    models = {
        u'erpapp.erpinquiry': {
            'Meta': {'object_name': 'ERPInquiry'},
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'company_website': ('django.db.models.fields.URLField', [], {'max_length': '75'}),
            'created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'message': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'product': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'update': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['erpapp']