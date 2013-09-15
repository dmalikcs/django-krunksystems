from django.db import models
from django import forms
from django.core.exceptions import ValidationError


def MobileValid(value):
    if  not (len(str(value))>=6 and len(str(value))<= 10):
        raise ValidationError(u'incorrect mobile number')

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
    course_logo=models.ImageField(upload_to='upload/courses/',
            blank=True,
            null=True,
            )
    course_name=models.CharField(verbose_name='Course',
            unique=True,
            max_length=50,
            blank=False,
            null=False,
            )
    course_short_description=models.CharField(verbose_name='Short description',
            max_length=50,
            )
    cource_detail=models.TextField(verbose_name='Course description',
            max_length=500,
            blank=False,
            null=False,
            )
    prerequisite=models.TextField(verbose_name='prerequisite',
            max_length=200,
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
            validators=[MobileValid]
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
            max_length=20,
            )
    intership_period=models.IntegerField(verbose_name='Intership Period',
            )
    platform=models.CharField(verbose_name='platform',
            choices=platforms,
            max_length=50,
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
class TrainingSuccess(models.Model):
    training_id=models.ForeignKey('TrainingCourse',
            related_name='success_stories',
            )
    customer_logo=models.ImageField(verbose_name='Image',
            upload_to='upload/training_success/',
            default='upload/training_success/ghaziabad100x100.jpg',
            )
    customer_name=models.CharField(verbose_name='Customer name',
            max_length=70
            )
    customer_email=models.EmailField(verbose_name='Email',
            )
    success_stories=models.TextField(verbose_name="Success Story",
            max_length=200,
            )
    def __unicode__(self):
        return u'%s' % self.training_id.course_name
    class Meta:
        verbose_name='Success Story'
        verbose_name_plural='Success Stories'

class CourseOutline(models.Model):
    training_id=models.ForeignKey('TrainingCourse',verbose_name='Training id',
            related_name='Course_outlines',
            )
    chapter=models.IntegerField(verbose_name='Chapter')
    topic=models.CharField(verbose_name='Topics',
            max_length=75,
            )
    hours=models.IntegerField(verbose_name='hours',
            )
    basics=models.TextField(verbose_name='Basics',
            max_length=200,
            )
    intermediate=models.TextField(verbose_name='intermediate' ,
            max_length=200,
            )
    Advance=models.TextField(verbose_name='Advance',
            max_length=200,
            )
    description=models.TextField(verbose_name='Description',
            max_length=200,
            )
    def __unicode__(self):
        return self.training_id.course_name
    class Meta:
        verbose_name='Course Outline'
        verbose_name_plural='Course Outlines'

class MentorDetail(models.Model):
    training_id=models.ManyToManyField('TrainingCourse',verbose_name='Training id',
            related_name='mentors',
            )
    name=models.CharField(verbose_name='mentor name',
            max_length=75,
            )
    mentor_images=models.ImageField(upload_to='upload/mentor_images/',
            null=True,
            blank=True,
            )
    email=models.EmailField(verbose_name='Email',
            unique=True,
            )
    phone=models.IntegerField(verbose_name='phone',
            validators=[MobileValid],
            )
    experience=models.IntegerField(verbose_name='Exprience',
            )
    linked_in=models.URLField(verbose_name='Linkedin ',
            )
    description=models.TextField(verbose_name='Description',
            max_length=200,
            )
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name='Mentor'
        verbose_name_plural='Mentors'
class WhyThisTraining(models.Model):
    training_id=models.ForeignKey('TrainingCourse',verbose_name='Training id',
            related_name='whythistraining',
            )
    why_this=models.TextField(verbose_name='why',
            max_length=60,
            )
    def __unicode__(self):
        return self.training_id.course_name
    class Meta:
        verbose_name='why'
        verbose_name_plural='why this Training'
    

class CorporateTrainingForm(forms.ModelForm):
    class Meta:
        model=CorporateTraining
        widgets ={ 'personal_email':forms.TextInput(attrs={ }) }

class TrainingCourseFrom(forms.ModelForm):
    class Meta:
        model=TrainingCourse


class IndustrialTrainingForm(forms.ModelForm):
    class Meta:
        model=IndustrialTraining

class AcademyTrainingForm(forms.ModelForm):
    class Meta:
        model=AcademyTraining
