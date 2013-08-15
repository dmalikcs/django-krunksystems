# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OpenERPModules'
        db.create_table(u'erpapp_openerpmodules', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('module_name', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('module_description', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('module_Features', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'erpapp', ['OpenERPModules'])

        # Adding model 'ErpCustomers'
        db.create_table(u'erpapp_erpcustomers', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('customer_name', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('testimonials', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('company_name', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('company_site', self.gf('django.db.models.fields.URLField')(max_length=100)),
        ))
        db.send_create_signal(u'erpapp', ['ErpCustomers'])

        # Adding M2M table for field modules on 'ErpCustomers'
        db.create_table(u'erpapp_erpcustomers_modules', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('erpcustomers', models.ForeignKey(orm[u'erpapp.erpcustomers'], null=False)),
            ('openerpmodules', models.ForeignKey(orm[u'erpapp.openerpmodules'], null=False))
        ))
        db.create_unique(u'erpapp_erpcustomers_modules', ['erpcustomers_id', 'openerpmodules_id'])


    def backwards(self, orm):
        # Deleting model 'OpenERPModules'
        db.delete_table(u'erpapp_openerpmodules')

        # Deleting model 'ErpCustomers'
        db.delete_table(u'erpapp_erpcustomers')

        # Removing M2M table for field modules on 'ErpCustomers'
        db.delete_table('erpapp_erpcustomers_modules')


    models = {
        u'erpapp.erpcustomers': {
            'Meta': {'object_name': 'ErpCustomers'},
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'company_site': ('django.db.models.fields.URLField', [], {'max_length': '100'}),
            'customer_name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'modules': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'modules_client'", 'symmetrical': 'False', 'to': u"orm['erpapp.OpenERPModules']"}),
            'testimonials': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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
            'product': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'update': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'erpapp.openerpmodules': {
            'Meta': {'object_name': 'OpenERPModules'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'module_Features': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'module_description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'module_name': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        }
    }

    complete_apps = ['erpapp']