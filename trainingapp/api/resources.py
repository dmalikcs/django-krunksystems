from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import Authorization
from trainingapp.models import TrainingCourse,CorporateTraining,IndustrialTraining,AcademyTraining,CorporateTrainingForm,TrainingSuccess,CourseOutline,MentorDetail,WhyThisTraining,IndustrialTrainingForm,AcademyTrainingForm
from tastypie.validation import Validation,FormValidation
from tastypie import fields

class TrainingCoursesResource(ModelResource):
    stories=fields.ToManyField('trainingapp.api.resources.TrainingSuccessResource','success_stories',null=True,full=True)
    course_outline=fields.ToManyField('trainingapp.api.resources.CourseOutlineResource','Course_outlines',null=True,full=True)
    mentors=fields.ToManyField('trainingapp.api.resources.MentorDetailResource','mentors',null=True,full=True)
    why=fields.ToManyField('trainingapp.api.resources.WhyThisTrainingResource','whythistraining',null=True,full=True)
    class Meta:
        queryset=TrainingCourse.objects.all()
        resource_name='courses'
        allowed_methods=['get']
        list_allowed_methods = ['get', 'post']
        #authentication=ApiKeyAuthentication()
        authorization=Authorization()
class TrainingSuccessResource(ModelResource):
    #trainings=fields.ForeignKey(TrainingCoursesResource,'training_id')
    #def dehydrate(self,bundle):
    #    print bundle.request
    #    return bundle
    class Meta:
        queryset=TrainingSuccess.objects.all()
        resource_name='stories'
        list_allowed_methods = ['get', 'post']
        allowed_methods=['get']
        authorization=Authorization()
class CourseOutlineResource(ModelResource):
    class Meta:
        queryset=CourseOutline.objects.all()
        resource_name='course_outline'
class MentorDetailResource(ModelResource):
    class Meta:
        queryset=MentorDetail.objects.all()
        allowed_methods=['get']
        resource_name='mentors'
class WhyThisTrainingResource(ModelResource):
    class Meta:
        queryset=WhyThisTraining.objects.all()
        resource_name='why'
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
        detail_allowed_methods=['post']
        authentication=ApiKeyAuthentication()
        authorization=Authorization()
        validation=FormValidation(form_class=IndustrialTrainingForm)

class AcademyTrainingResource(ModelResource):
    class Meta:
        queryset=AcademyTraining.objects.all()
        resource_name='ac_training'
        allowed_methods=['get','post']
        authentication=ApiKeyAuthentication()
        authorization=Authorization()
        validation=FormValidation(form_class=AcademyTrainingForm)


