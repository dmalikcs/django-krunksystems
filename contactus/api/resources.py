from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import Authorization
from contactus.models import A2M1_contactus,A2F1_contactus
from tastypie.validation import Validation,FormValidation
from tastypie import fields


class ContactusResource(ModelResource):
    class Meta:
        queryset=A2M1_contactus.objects.all()
        resource_name='contactus'
        allowed_methods=['get','post']
        authentication=ApiKeyAuthentication()
        authorization=Authorization()
        validation=FormValidation(form_class=A2F1_contactus)


