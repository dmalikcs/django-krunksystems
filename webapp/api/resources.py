from tastypie.resources import ModelResource
from tastypie.authentication import Authentication

from webapp.models import Development

class DevelopmentResource(ModelResource):
    class Meta:
        queryset=Development.objects.all()
        resource_name='development'
