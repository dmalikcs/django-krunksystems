from tastypie.resources import ModelResource 
from tastypie.authentication import Authentication 

from Consultancyapp.models import PythonConsultancy,DjangoConsultancy,OpensourceConsultancy,MidrangeConsultancy


class PythonConsultancyResource(ModelResource):
    class Meta:
        queryset=PythonConsultancy.objects.all()
        resource_name='python'

class DjangoConsultancyResource(ModelResource):
    class Meta:
        queryset=DjangoConsultancy.objects.all()
        resource_name='django'

class OpensourceConsultancyResource(ModelResource):
    class Meta:
        queryset=OpensourceConsultancy.objects.all()
        resource_name='os'

class MidrangeConsultancyResource(ModelResource):
    class Meta:
        queryset=MidrangeConsultancy.objects.all()
        resource_name='midrange'
