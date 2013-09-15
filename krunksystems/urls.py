from django.conf.urls import patterns, include, url
from krunksystems import settings
from tastypie.api import Api
from trainingapp.api.resources import TrainingCoursesResource,CorporateTrainingResource,IndustrialTrainingResource,AcademyTrainingResource,TrainingSuccessResource
from Consultancyapp.api.resources import PythonConsultancyResource,DjangoConsultancyResource,OpensourceConsultancyResource,MidrangeConsultancyResource
from webapp.api.resources import DevelopmentResource
from erpapp.api.resources import OpenERPModulesResource,ERPInquiryResource,ErpDemoResource,ERPModuleDetailResource
from contactus.api.resources import ContactusResource
v1_api=Api(api_name='v1')
v1_api.register(TrainingCoursesResource())
v1_api.register(CorporateTrainingResource())
v1_api.register(IndustrialTrainingResource())
v1_api.register(AcademyTrainingResource())
v1_api.register(PythonConsultancyResource())
v1_api.register(DjangoConsultancyResource())
v1_api.register(OpensourceConsultancyResource())
v1_api.register(MidrangeConsultancyResource())
v1_api.register(DevelopmentResource())
v1_api.register(OpenERPModulesResource())
v1_api.register(TrainingSuccessResource())
v1_api.register(ERPInquiryResource())
v1_api.register(ErpDemoResource())
v1_api.register(ContactusResource())
v1_api.register(ERPModuleDetailResource())

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'landingapp.views.A1V1_landing', name='A1V1_landing_url'),
    url(r'^contactus/$', 'contactus.views.A2V1_contactus', name='contactus_url'),
    # url(r'^krunksystems/', include('krunksystems.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/',include(v1_api.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
    url(r'%s(?P<path>.*)' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    )
