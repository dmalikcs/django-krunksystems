from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import Authorization
from tastypie.validation import Validation,FormValidation
from tastypie import fields
from ..models import OpenERPModules,ERPInquiry,ERPInquiryForm,ErpDemo,ErpDemoForm,ERPTraining,ErpCustomers
import json


class OpenERPModulesResource(ModelResource):
    class Meta:
        queryset=OpenERPModules.objects.all()
        resource_name='modules'
        allowed_methods=['get']
        detail_allowed_methods=['get']
        limit=3
        #authentication=ApiKeyAuthentication()
        #authorization=Authorization()
        #validation=FormValidation(form_class=CorporateTrainingForm)

class ERPInquiryResource(ModelResource):
    class Meta:
        queryset=ERPInquiry.objects.all()
        resource_name='inquiry'
        allowed_method=['POST',]
        authentication=ApiKeyAuthentication()
        authorization=Authorization()
        validation=FormValidation(form_class=ERPInquiryForm)

class ErpDemoResource(ModelResource):
    modules=fields.ToManyField(to=OpenERPModulesResource,attribute='modules',related_name='customer_modules_demo',full=True)
    def hydrate_m2m(self,bundle):
        try:
            modules_ids = map(lambda x: int(x), bundle.data.get('modules', []))
        except ValueError:
           raise BadRequest("User ids must be ints") # from tastypie.exceptions
        bundle.data['modules'] = OpenERPModules.objects.filter(id__in=modules_ids)
        return super(ErpDemoResource,self).hydrate_m2m(bundle)
    class Meta:
        queryset=ErpDemo.objects.all()
        resource_name='demorequest'
        allowed_method=['GET','POST',]
        authentication=ApiKeyAuthentication()
        authorization=Authorization()
        validation=FormValidation(form_class=ErpDemoForm)

class ERPTrainingResource(ModelResource):
    class Meta:
        queryset=ERPTraining.objects.all()
        resource_name='erp_training'
        allowed_methods=['get',]

class ErpCustomersResource(ModelResource):
    class Meta:
        queryset=ErpCustomers.objects.all()
        resource_name='erp_customers'
        allowed_methods=['get',]

class ERPModuleDetailResource(ModelResource):
    trainings=fields.ToOneField(ERPTrainingResource,'ERP_trainings',full=True,null=True)
    customer_kind_words=fields.ToManyField(ErpCustomersResource,'modules_client',full=True,null=True)
    class Meta:
        queryset=OpenERPModules.objects.all()
        resource_name='modules_detail'
        allowed_methods=['get']
        detail_allowed_methods=['get']
