# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'AcademyTraining.degree'
        db.alter_column(u'trainingapp_academytraining', 'degree', self.gf('django.db.models.fields.CharField')(max_length=10))

        # Changing field 'AcademyTraining.branch'
        db.alter_column(u'trainingapp_academytraining', 'branch', self.gf('django.db.models.fields.CharField')(max_length=10))

        # Changing field 'AcademyTraining.message'
        db.alter_column(u'trainingapp_academytraining', 'message', self.gf('django.db.models.fields.TextField')(max_length=200))

    def backwards(self, orm):

        # Changing field 'AcademyTraining.degree'
        db.alter_column(u'trainingapp_academytraining', 'degree', self.gf('django.db.models.fields.CharField')(max_length=3))

        # Changing field 'AcademyTraining.branch'
        db.alter_column(u'trainingapp_academytraining', 'branch', self.gf('django.db.models.fields.CharField')(max_length=2))

        # Changing field 'AcademyTraining.message'
        db.alter_column(u'trainingapp_academytraining', 'message', self.gf('django.db.models.fields.CharField')(max_length=200))

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