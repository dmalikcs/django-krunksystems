# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CorporateTraining'
        db.create_table(u'trainingapp_corporatetraining', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company_name', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('employee_name', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('personal_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('offical_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('mobile', self.gf('django.db.models.fields.IntegerField')()),
            ('phone', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'trainingapp', ['CorporateTraining'])


    def backwards(self, orm):
        # Deleting model 'CorporateTraining'
        db.delete_table(u'trainingapp_corporatetraining')


    models = {
        u'trainingapp.corporatetraining': {
            'Meta': {'object_name': 'CorporateTraining'},
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'employee_name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile': ('django.db.models.fields.IntegerField', [], {}),
            'offical_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'personal_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'phone': ('django.db.models.fields.IntegerField', [], {})
        },
        u'trainingapp.trainingcourse': {
            'Meta': {'object_name': 'TrainingCourse'},
            'cource_detail': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'course_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'hours': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['trainingapp']