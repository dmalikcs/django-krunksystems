# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ErpDemo'
        db.create_table(u'erpapp_erpdemo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('customer_id', self.gf('django.db.models.fields.related.ForeignKey')(related_name='customer_erpdemo', to=orm['erpapp.ERPInquiry'])),
            ('modules', self.gf('django.db.models.fields.related.ForeignKey')(related_name='customer_modules_demo', to=orm['erpapp.OpenERPModules'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('time', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal(u'erpapp', ['ErpDemo'])

        # Adding field 'ERPInquiry.phone'
        db.add_column(u'erpapp_erpinquiry', 'phone',
                      self.gf('django.db.models.fields.IntegerField')(default=None),
                      keep_default=False)


        # Changing field 'ErpCustomers.testimonials'
        db.alter_column(u'erpapp_erpcustomers', 'testimonials', self.gf('django.db.models.fields.TextField')(max_length=200))

        # Changing field 'OpenERPModules.module_description'
        db.alter_column(u'erpapp_openerpmodules', 'module_description', self.gf('django.db.models.fields.TextField')(max_length=100))

        # Changing field 'OpenERPModules.module_Features'
        db.alter_column(u'erpapp_openerpmodules', 'module_Features', self.gf('django.db.models.fields.TextField')(max_length=300))

    def backwards(self, orm):
        # Deleting model 'ErpDemo'
        db.delete_table(u'erpapp_erpdemo')

        # Deleting field 'ERPInquiry.phone'
        db.delete_column(u'erpapp_erpinquiry', 'phone')


        # Changing field 'ErpCustomers.testimonials'
        db.alter_column(u'erpapp_erpcustomers', 'testimonials', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'OpenERPModules.module_description'
        db.alter_column(u'erpapp_openerpmodules', 'module_description', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'OpenERPModules.module_Features'
        db.alter_column(u'erpapp_openerpmodules', 'module_Features', self.gf('django.db.models.fields.CharField')(max_length=300))

    models = {
        u'erpapp.erpcustomers': {
            'Meta': {'object_name': 'ErpCustomers'},
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'company_site': ('django.db.models.fields.URLField', [], {'max_length': '100'}),
            'customer_name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'modules': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'modules_client'", 'symmetrical': 'False', 'to': u"orm['erpapp.OpenERPModules']"}),
            'testimonials': ('django.db.models.fields.TextField', [], {'max_length': '200'})
        },
        u'erpapp.erpdemo': {
            'Meta': {'object_name': 'ErpDemo'},
            'customer_id': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'customer_erpdemo'", 'to': u"orm['erpapp.ERPInquiry']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modules': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'customer_modules_demo'", 'to': u"orm['erpapp.OpenERPModules']"}),
            'time': ('django.db.models.fields.TimeField', [], {})
        },
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
            'phone': ('django.db.models.fields.IntegerField', [], {}),
            'product': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'update': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'erpapp.openerpmodules': {
            'Meta': {'object_name': 'OpenERPModules'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'module_Features': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'module_description': ('django.db.models.fields.TextField', [], {'max_length': '100'}),
            'module_name': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        }
    }

    complete_apps = ['erpapp']