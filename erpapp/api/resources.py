from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import Authorization
from tastypie.validation import Validation,FormValidation
from ..models import OpenERPModules


class OpenERPModulesResource(ModelResource):
    def hydrate(self,bundle):
        print bundle.request.POST
        return bundle
    class Meta:
        queryset=OpenERPModules.objects.all()
        resource_name='modules'
        allowed_methods=['get']
        detail_allowed_methods=['get']
        #authentication=ApiKeyAuthentication()
        #authorization=Authorization()
        #validation=FormValidation(form_class=CorporateTrainingForm)

