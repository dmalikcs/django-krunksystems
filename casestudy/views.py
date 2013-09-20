from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import CaseStudyModel,CaseStudyDocs

class CaseStudyView(ListView):
    model=CaseStudyModel
    context_object_name='casestudies'


class CaseStudyDetailView(DetailView):
    model=CaseStudyModel
    context_object_name='casestudy'
    def get_context_data(self, **kwargs):
        context=super(CaseStudyDetailView,self).get_context_data(**kwargs)
        context['docs']=CaseStudyDocs.objects.filter(CaseStudyid_id=self.object.id)
        print context['docs']
        return context
    def get_object(self):
        object=super(CaseStudyDetailView,self).get_object()
        print dir(object.frameworks)
        print dir(object)
        return object

