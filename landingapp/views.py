# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext 
from django.shortcuts import render_to_response

def A1V1_landing(request):
    template_name="index.html"
    template_dic={}
    ci=RequestContext(request)
    return render_to_response(
            template_name,
            template_dic,
            ci
            )
