# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import feedbackModelForm,feedback
from django.views.generic.edit import CreateView


class feedbackView(CreateView):
    model=feedback
    template_name='feedback.html'
    form_class=feedbackModelForm
    success_url='/thanks/'
