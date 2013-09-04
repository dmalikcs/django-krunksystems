from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import Authorization
from tastypie.validation import Validation,FormValidation
from tastypie import fields

from Consultancyapp.models import PythonConsultancy,DjangoConsultancy,OpensourceConsultancy,MidrangeConsultancy,PythonConsultancyForm,DjangoConsultancyForm,OpensourceConsultancyForm,MidrangeConsultancyForm


class PythonConsultancyResource(ModelResource):
    class Meta:
        queryset=PythonConsultancy.objects.all()
        resource_name='python'
        allowed_methods=['get','post']
        authorization=Authorization()
        authentication=ApiKeyAuthentication()
        validation=FormValidation(form_class=PythonConsultancyForm)

class DjangoConsultancyResource(ModelResource):
    class Meta:
        queryset=DjangoConsultancy.objects.all()
        resource_name='django'
        allowed_methods=['get','post']
        authorization=Authorization()
        authentication=ApiKeyAuthentication()
        validation=FormValidation(form_class=DjangoConsultancyForm)

class OpensourceConsultancyResource(ModelResource):
    class Meta:
        queryset=OpensourceConsultancy.objects.all()
        resource_name='os'
        allowed_methods=['get','post']
        authorization=Authorization()
        authentication=ApiKeyAuthentication()
        validation=FormValidation(form_class=OpensourceConsultancyForm)

class MidrangeConsultancyResource(ModelResource):
    class Meta:
        queryset=MidrangeConsultancy.objects.all()
        resource_name='midrange'
        allowed_methods=['get','post']
        authorization=Authorization()
        authentication=ApiKeyAuthentication()
        validation=FormValidation(form_class=MidrangeConsultancyForm)
