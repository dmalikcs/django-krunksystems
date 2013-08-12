from django.http import HttpResponse
from django.template import RequestContext 
from django.shortcuts import render_to_response


from .models import A2F1_contactus,A2M1_contactus

# Create your views here.


def A2V1_contactus(request):
    '''
    Contact us page desiged for Krunksystems.com 
    Worked with Ajax        # Not yet
    Worked with Post method # Tested

    '''
    template_dic={}
    ci=RequestContext(request)
    template_dic['contactus_form']=A2F1_contactus(request.POST if request.method=='POST' else None)
    if request.is_ajax():
        template_name="contactus_ajax.html"
        if request.method=='POST':
           if  template_dic['contactus_form'].is_valid():
               contactus_data=template_dic['contactus_form'].cleaned_data
               try:
                    A2M1_contactus.objects.create(**contactus_data)
                    print "Database been successfully saved"            
               except:
                    print "Return to log files"
               return HttpResponse('Data has been successfully created')
           else:
                return render_to_response(template_name,
                        template_dic,
                        ci
                        )
        else:
            return render_to_response(template_name,
                    template_dic,
                    ci
                    )
    else:
        template_name="contactus_post.html"
        if request.method=='POST':
            if  template_dic['contactus_form'].is_valid():
                contactus_data=template_dic['contactus_form'].cleaned_data
                try:
                    A2M1_contactus.objects.create(**contactus_data)
                    print "Database been successfully saved"
                except:
                    print "Return to log files"
                return HttpResponse('Data has been successfully created')
            else:
                return render_to_response(template_name,
                        template_dic,
                        ci
                        )
        else:
            return render_to_response(template_name,
                    template_dic,
                    ci
                    )
