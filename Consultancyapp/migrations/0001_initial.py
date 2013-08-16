# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PythonConsultancy'
        db.create_table(u'Consultancyapp_pythonconsultancy', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('message', self.gf('django.db.models.fields.TextField')(max_length=500)),
        ))
        db.send_create_signal(u'Consultancyapp', ['PythonConsultancy'])


    def backwards(self, orm):
        # Deleting model 'PythonConsultancy'
        db.delete_table(u'Consultancyapp_pythonconsultancy')


    models = {
        u'Consultancyapp.pythonconsultancy': {
            'Meta': {'object_name': 'PythonConsultancy'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['Consultancyapp']