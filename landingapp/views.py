# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext 
from django.shortcuts import render_to_response
from trainingapp.models import CorporateTrainingForm,IndustrialTrainingForm,AcademyTrainingForm
from webapp.models import DevelopmentForm
from erpapp.models import ERPInquiryForm,ErpDemoForm,ErpCustomersForm
from Consultancyapp.models import PythonConsultancyForm,DjangoConsultancyForm,OpensourceConsultancyForm,MidrangeConsultancyForm
from contactus.models import A2F1_contactus,A2M1_contactus

def A1V1_landing(request):
    template_name="index.html"
    template_dic={}
    template_dic['contactus_form']=A2F1_contactus()
    template_dic['ct_Form']=CorporateTrainingForm()
    template_dic['it_Form']=IndustrialTrainingForm()
    template_dic['at_Form']=AcademyTrainingForm()
    template_dic['development_Form']=DevelopmentForm()
    template_dic['erpinquiry_Form']=ERPInquiryForm()
    template_dic['erpdemo_Form']=ErpDemoForm()
    template_dic['erpcustomer_Form']=ErpCustomersForm()
    template_dic['python_Form']=PythonConsultancyForm()
    template_dic['django_Form']=DjangoConsultancyForm()
    template_dic['opensource_Form']=OpensourceConsultancyForm()
    template_dic['midrange_Form']=MidrangeConsultancyForm()
    ci=RequestContext(request)
    return render_to_response(
            template_name,
            template_dic,
            ci
            )
