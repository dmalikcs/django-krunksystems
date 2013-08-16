from django.db import models
from django import forms
type_of_training=(
        ('Corporate','CT'),
        ('Industrial','IT'),
        ('Academy','AT'),
        )
degrees=(
        ('B-tech','bt'),
        ('BSc','bsc'),
        ('MSc','msc'),
        ('MTech','mtech'),
        ('Phd','phd'),
        )
branches=(
        ('B-tech','bt'),
        ('BSc','bsc'),
        ('MSc','msc'),
        ('MTech','mtech'),
        )
platforms=(
        ('web Development','WB'),
        ('web Development','WB'),
        ('web Development','WB'),
        )
class TrainingCourse(models.Model):
    course_name=models.CharField(verbose_name='Course',
            unique=True,
            max_length=50,
            blank=False,
            null=False,
            )
    cource_detail=models.TextField(verbose_name='Course description',
            max_length=500,
            blank=False,
            null=False,
            )
    hours=models.IntegerField(verbose_name='Hours',
            )
    created=models.DateField(verbose_name='Created',
            auto_now_add=True
            )
    modified=models.DateField(verbose_name='Modified',
            auto_now=True,
            auto_now_add=True,
            )
    def __unicode__(self):
        return self.course_name
    class Meta:
        verbose_name='Training Course'
        verbose_name_plural='Training Courses'

class CorporateTraining(models.Model):
    company_name=models.CharField(verbose_name='Company Name',
            max_length=75,
            blank=False,
            null=False,
            unique=False, 
            )
    employee_name=models.CharField(verbose_name='employee name',
            max_length=75,
            blank=False,
            null=False, 
            )
    personal_email=models.EmailField(verbose_name='Personal email',
            )
    offical_email=models.EmailField(verbose_name='Offical email',
            )
    mobile=models.IntegerField(verbose_name='Mobile',
            )
    phone=models.IntegerField(verbose_name='phone',
            )
    message=models.TextField(verbose_name='Message',
            max_length=500,
            )

    def __unicode__(self):
        return self.employee_name

    class Meta:
        verbose_name='Coporrate Training'
        verbose_name_plural='Corporate Trainings'
class IndustrialTraining(models.Model):
    student_name=models.CharField(verbose_name='name',
            max_length=75,
            )
    email=models.EmailField(verbose_name='email',
            )
    mobile=models.IntegerField(verbose_name='mobile'
            )
    collage=models.CharField(verbose_name='collage',
            max_length=75,
            )
    degree=models.CharField(verbose_name='Degree',
            choices=degrees,
            max_length=10,
            )
    intership_period=models.IntegerField(verbose_name='Intership Period',
            )
    platform=models.CharField(verbose_name='platform',
            choices=platforms,
            max_length=10,
            )
    message=models.TextField(verbose_name='Messgae',
            max_length=200,
            )
    def __unicode__(self):
        return self.student_name
    class Meta:
        verbose_name='Industrial Training'
        verbose_name_plural='Industrial Trainings'



class AcademyTraining(models.Model):
    student_name=models.CharField(verbose_name='name',
            max_length=75,
            )
    email=models.EmailField(verbose_name='email',
            )
    degree=models.CharField(verbose_name='Degree',
            choices=degrees,
            max_length=10,
            )
    branch=models.CharField(verbose_name='Branch',
            choices=branches,
            max_length=10,
            )
    mobile=models.IntegerField(verbose_name='mobile',
            )

    collage_name=models.CharField(verbose_name='Collage name',
            max_length=75,
            )
    collage_website=models.URLField(verbose_name='website',
            max_length=75,
            )
    message=models.TextField(verbose_name='messgae',
            max_length=200,
            )
    def __unicode__(self):
        return self.student_name
    class Meta:
        verbose_name='Academy Training'
        verbose_name_plural='Academy Trainings'


class CorporateTrainingForm(forms.ModelForm):
    class Meta:
        model=CorporateTraining
