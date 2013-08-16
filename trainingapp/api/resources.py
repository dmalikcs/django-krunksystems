from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import Authorization
from trainingapp.models import TrainingCourse,CorporateTraining,IndustrialTraining,AcademyTraining

class TrainingCourseResource(ModelResource):
    class Meta:
        queryset=TrainingCourse.objects.all()
        resource_name='trainingcource'
        allowed_methods=['get','post']
        #authentication=ApiKeyAuthentication()
        #authorization=Authorization()

class CorporateTrainingResource(ModelResource):
    class Meta:
        queryset=CorporateTraining.objects.all()
        resource_name='cor_training'
        allowed_methods=['get','post']
        authentication=ApiKeyAuthentication()
        authorization=Authorization()

class IndustrialTrainingResource(ModelResource):
    class Meta:
        queryset=IndustrialTraining.objects.all()
        resource_name='id_training'
        allowed_methods=['get','post']
        authentication=ApiKeyAuthentication()
        authorization=Authorization()

class AcademyTrainingResource(ModelResource):
    class Meta:
        queryset=AcademyTraining.objects.all()
        resource_name='ac_training'
        allowed_methods=['get','post']
        authentication=ApiKeyAuthentication()
        authorization=Authorization()


