from django.db import models
from django import forms

class ERPInquiry(models.Model):
    name=models.CharField(verbose_name='name',
            max_length=60,
            )
    job_title=models.CharField(verbose_name='Job Title',
            max_length=50,
            )
    phone=models.IntegerField(verbose_name='Mobile',
            )
    email=models.EmailField(verbose_name='Email',
            )
    company_name=models.CharField(verbose_name='Company Name',
            max_length=75,
            )
    company_website=models.URLField(verbose_name='website',
            max_length=75,
            )
    product=models.CharField(verbose_name='Products',
            max_length=75,
            )
    message=models.TextField(verbose_name='your message',
            max_length=200,
            )
    created=models.DateField(verbose_name='created',
            auto_now_add=True
            )
    update=models.DateField(verbose_name='update',
            auto_now_add=True,
            auto_now=True,
            )

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name='OpenERP Inquiry'
        verbose_name_plural='OpenERP Inquiries'

class OpenERPModules(models.Model):
    module_image=models.ImageField(verbose_name='Module image',
            upload_to='upload/openerp_images/'
            )
    module_name=models.CharField(verbose_name='Module name',
            max_length=70,
            )
    module_short_description=models.TextField(verbose_name='Brief description',
            max_length=100,
            )
    module_description=models.TextField(verbose_name='Description',
            max_length=100,
            )
    module_Features=models.TextField(verbose_name='Features',
            max_length=300,
            )
    def __unicode__(self):
        return self.module_name
    class Meta:
        verbose_name='Module'
        verbose_name_plural='Modules'

class ErpDemo(models.Model):
    name=models.CharField(verbose_name='Name',
            max_length=60,
            )
    mobile=models.IntegerField(verbose_name='Mobile',
            )
    email=models.EmailField(verbose_name='email',
            unique=True,
            )
    modules=models.ManyToManyField(OpenERPModules,
            verbose_name='modules',
            related_name='customer_modules_demo',
            )
    Type_of_demo=models.CharField(verbose_name='Demo',
            max_length=20,
            choices=(('R','Remote'),('S','On-site')),
            )
    date=models.DateField(verbose_name='Demo Date'
            )
    time=models.TimeField(verbose_name='Demo Time',
            )
    requested_date=models.DateField(auto_now_add=True
            )
    status=models.CharField(verbose_name='Status',
            max_length=30,
            default='New',
            )
    def __unicode__(self):
        return  self.name
    class Meta:
        verbose_name='Erp Demo'
        verbose_name='Erp Demos'

class ErpCustomers(models.Model):
    modules=models.ManyToManyField(OpenERPModules,
            verbose_name='modules',
            related_name='modules_client'
            )
    customer_name=models.CharField(verbose_name='Customer Name',
            max_length=75,
            )
    logo=models.ImageField(verbose_name='logo',
            upload_to='logs/',
            null=True,
            blank=True,
            )
    testimonials=models.TextField(verbose_name='testimonials',
            max_length=200,
            )
    company_name=models.CharField(verbose_name='Company Name',
            max_length=70,
            )
    company_site=models.URLField(verbose_name='company urls',
            max_length=100,
            )
    def __unicode__(self):
        return self.customer_name
    class Meta:
        verbose_name='ERP Customer'
        verbose_name_plural='ERP Customers'

class ERPTraining(models.Model):
    modules=models.OneToOneField(OpenERPModules,verbose_name='Modules',
            related_name='ERP_trainings'
            )
    technical_training=models.TextField(verbose_name='Technical Training',
            max_length=500,
            )
    Functional_training=models.TextField(verbose_name='Functional Training',
            max_length=500,
            )
    def __unicode__(self):
        return self.modules.module_name
    class Meta:
        verbose_name='Erp Training'
        verbose_name_plural='Erp Trainings'

class ERPInquiryForm(forms.ModelForm):
    class Meta:
        model=ERPInquiry

class OpenERPModulesForm(forms.ModelForm):
    class Meta:
        model=OpenERPModules

class ErpDemoForm(forms.ModelForm):
    class Meta:
        model=ErpDemo
        exclude=['status']
        widgets ={ 
                    'modules':forms.SelectMultiple(),
                }

class ErpCustomersForm(forms.ModelForm):
    class Meta:
        model=ErpCustomers

# Create your models here.
