# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'IndustrialTraining'
        db.create_table(u'trainingapp_industrialtraining', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student_name', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('mobile', self.gf('django.db.models.fields.IntegerField')()),
            ('collage', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('degree', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('intership_period', self.gf('django.db.models.fields.IntegerField')()),
            ('platform', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'trainingapp', ['IndustrialTraining'])


    def backwards(self, orm):
        # Deleting model 'IndustrialTraining'
        db.delete_table(u'trainingapp_industrialtraining')


    models = {
        u'trainingapp.academytraining': {
            'Meta': {'object_name': 'AcademyTraining'},
            'branch': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'collage_name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'collage_website': ('django.db.models.fields.URLField', [], {'max_length': '75'}),
            'degree': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'mobile': ('django.db.models.fields.IntegerField', [], {}),
            'student_name': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        },
        u'trainingapp.corporatetraining': {
            'Meta': {'object_name': 'CorporateTraining'},
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'employee_name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'mobile': ('django.db.models.fields.IntegerField', [], {}),
            'offical_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'personal_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'phone': ('django.db.models.fields.IntegerField', [], {})
        },
        u'trainingapp.industrialtraining': {
            'Meta': {'object_name': 'IndustrialTraining'},
            'collage': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'degree': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intership_period': ('django.db.models.fields.IntegerField', [], {}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'mobile': ('django.db.models.fields.IntegerField', [], {}),
            'platform': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'student_name': ('django.db.models.fields.CharField', [], {'max_length': '75'})
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