from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import Authorization
from tastypie.validation import Validation,FormValidation
from tastypie import fields

from webapp.models import Development,DevelopmentForm

class DevelopmentResource(ModelResource):
    file=fields.FileField(attribute='project_file',null=True,blank=True)
    class Meta:
        queryset=Development.objects.all()
        resource_name='development'
        allowed_methods=['get','post']
        authorization=Authorization()
        authentication=ApiKeyAuthentication()
        validation=FormValidation(form_class=DevelopmentForm)
