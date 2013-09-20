from django.db import models

class DjangoInbuildFramework(models.Model):
    dj_name=models.CharField(verbose_name='Django framework',
            max_length=100,
            )
    dj_description=models.TextField(verbose_name='Description',
            max_length=200,
            )
    def __unicode__(self):
        return self.dj_name
    class Meta:
        verbose_name='Django inbuild framework '
        verbose_name_plural='Django imbuild frameworks'
    

class FrameworkUsed(models.Model):
    framework_name=models.CharField(verbose_name='Framework name',
            max_length=30,
            )
    language=models.CharField(verbose_name='language',
            max_length=30,
            )
    def __unicode__(self):
        return self.framework_name
    class Meta:
        verbose_name='Framework'
        verbose_name_plural='Frameworks'

class Languages(models.Model):
    language=models.CharField(verbose_name='language',
            max_length=75
            )
    def __unicode__(self):
        return self.language
    class Meta:
        verbose_name='language'
        verbose_name_plural='lamguages'

class ProblemFaced(models.Model):
    problem=models.TextField(verbose_name='Problem',
            max_length=100,
            )
    solution=models.TextField(verbose_name='Solution',
            max_length=400,
            )
    def __unicode__(self):
        return self.problem
    class Meta:
        verbose_name='Problem'
        verbose_name_plural='problems'


class CaseStudyModel(models.Model):
    project_name=models.CharField(verbose_name='Project Name',
            max_length=100,
            )
    project_url=models.URLField(verbose_name='Project url',
            )
    git_url=models.URLField(verbose_name='Git Url',
            )
    languages=models.ManyToManyField('Languages',
            verbose_name='languages',
            related_name='languages',
            )
    frameworks=models.ManyToManyField('FrameworkUsed',
            verbose_name='frameworks',
            related_name='frameworks',
            )
    dj_frameworks=models.ManyToManyField('DjangoInbuildFramework',
            verbose_name='dj_frameworks',
            related_name='dj_frameworks',
            )
    brief=models.TextField(verbose_name='brief',
            max_length=200
            )
    description=models.TextField(verbose_name='description',
            max_length=500,
            )
    problems=models.ManyToManyField( 'ProblemFaced',
            verbose_name='Problems',
            related_name='problems',
            )
    start_date=models.DateField(verbose_name='Start Date',
            )
    end_date=models.DateField(verbose_name='End Date',
            )
    def __unicode__(self):
        return self.project_name
    class Meta:
        verbose_name='Case Study'
        verbose_name_plural='case Studies'

class CaseStudyDocs(models.Model):
    CaseStudyid=models.ForeignKey('CaseStudyModel',
            verbose_name='Case study',
            )
    doc_name=models.CharField(verbose_name='Document name',
            max_length=30
            )
    doc_attach=models.FileField(upload_to='upload/casestudy/',
            verbose_name='document'
            )
    docs_description=models.TextField(verbose_name='Document Description',
            max_length=100,
            )
    def __unicode__(self):
        return self.CaseStudyid.project_name
    class Meta:
        verbose_name="Case Study documnet"
        verbose_name_plural="Case Study documents"
