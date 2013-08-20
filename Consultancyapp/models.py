from django.db import models
from django import forms
python_categories=(
        ('Fi','Fiber'),
        ('Li','Linux'),
        )

django_categories=(
        ('dj','Django'),
        ('Developers','Django developer'),
        )

opensource_categories=(
        ('django','Django'),
        ('asterisk','OpenERP'),
        ('samba','samba'),
        )

midrange_categories=(
        ('vx','Veritas'),
        ('sx','Solaris'),
        )


class PythonConsultancy(models.Model):
    name=models.CharField(verbose_name='Name',
            max_length=50,
            )
    email=models.EmailField(verbose_name='email',
            )
    category=models.CharField(verbose_name='categories',
            max_length=10,
            choices=python_categories
            )
    message=models.TextField(verbose_name='Message',
            max_length=500
            )
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name="Python Consultancy"
        verbose_name_plural="Python Consultancies"


class DjangoConsultancy(models.Model):
    name=models.CharField(verbose_name='Name',
            max_length=50,
            )
    email=models.EmailField(verbose_name='email',
            )
    category=models.CharField(verbose_name='categories',
            max_length=10,
            choices=django_categories
            )
    message=models.TextField(verbose_name='Message',
            max_length=500
            )
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name="Django Consultancy"
        verbose_name_plural="Django Consultancies"

class OpensourceConsultancy(models.Model):
    name=models.CharField(verbose_name='Name',
            max_length=50,
            )
    email=models.EmailField(verbose_name='email',
            )
    category=models.CharField(verbose_name='categories',
            max_length=10,
            choices=opensource_categories
            )
    message=models.TextField(verbose_name='Message',
            max_length=500
            )
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name="OpenSource Consultancy"
        verbose_name_plural="OpenSource Consultancies"


class MidrangeConsultancy(models.Model):
    name=models.CharField(verbose_name='Name',
            max_length=50,
            )
    email=models.EmailField(verbose_name='email',
            )
    category=models.CharField(verbose_name='categories',
            max_length=10,
            choices=midrange_categories
            )
    message=models.TextField(verbose_name='Message',
            max_length=500
            )
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name="Midrange Consultancy"
        verbose_name_plural="Midrange Consultancies"


class PythonConsultancyForm(forms.ModelForm):
    class Meta:
        model=PythonConsultancy

class DjangoConsultancyForm(forms.ModelForm):
    class Meta:
        model=DjangoConsultancy

class OpensourceConsultancyForm(forms.ModelForm):
    class Meta:
        model=OpensourceConsultancy

class MidrangeConsultancyForm(forms.ModelForm):
    class Meta:
        model=MidrangeConsultancy
