from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import Authorization
from trainingapp.models import TrainingCourse,CorporateTraining,IndustrialTraining,AcademyTraining,CorporateTrainingForm
from tastypie.validation import Validation,FormValidation

class TrainingCoursesResource(ModelResource):
    class Meta:
        queryset=TrainingCourse.objects.all()
        #fields=['id','course_name',]
        resource_name='courses'
        allowed_methods=['get']
        #authentication=ApiKeyAuthentication()
        #authorization=Authorization()
class TrainingCourseResource(ModelResource):
    class Meta:
        queryset=TrainingCourse.objects.all()
        #fields=['id',]
        resource_name='courses'
        allowed_methods=['get']

class CorporateTrainingResource(ModelResource):
    def hydrate(self,bundle):
        print bundle.request.POST
        return bundle
    class Meta:
        queryset=CorporateTraining.objects.all()
        resource_name='cor_training'
        allowed_methods=['get','post']
        detail_allowed_methods=['post']
        authentication=ApiKeyAuthentication()
        authorization=Authorization()
        validation=FormValidation(form_class=CorporateTrainingForm)

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


