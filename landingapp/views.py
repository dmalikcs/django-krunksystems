# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext 
from django.shortcuts import render_to_response

from contactus.models import A2F1_contactus,A2M1_contactus

def A1V1_landing(request):
    template_name="index.html"
    template_dic={}
    template_dic['contactus_form']=A2F1_contactus()
    ci=RequestContext(request)
    return render_to_response(
            template_name,
            template_dic,
            ci
            )
