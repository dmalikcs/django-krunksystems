from django.db import models
from django import forms

status=(
        ('New','N'),
        ('review','R'),
        ('closed','C'),
        ('Followup','F'),
        )

class Development(models.Model):
    name=models.CharField(
            verbose_name='name',
            max_length=60,
            )
    email=models.EmailField(
            verbose_name='email',
            )
    country=models.CharField(
            verbose_name='country',
            max_length=50,
            )
    mobile=models.CharField(
            verbose_name='Phone/Skype',
            max_length=30,
            )
    project_budget=models.CharField(
            verbose_name='budget',
            max_length=7,
            )
    project_start_date=models.DateField(
            verbose_name='Project start date',
            )
    project_file=models.FileField(
            verbose_name='Details',
            upload_to='webapp_upload/',
            blank=True,
            null=True,
            )
    project_message=models.CharField(
            verbose_name='Message',
            max_length=200,
            )
    created=models.DateField(
            verbose_name='created',
            auto_now_add=True
            )
    update=models.DateField(
            verbose_name='update',
            auto_now=True,
            auto_now_add=True,
            )
    status=models.CharField(
            verbose_name='status',
            max_length=1,
            choices=status
            )
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name='Development'
        verbose_name_plural='Developments'

class DevelopmentForm(forms.ModelForm):
    class Meta:
        model=Development

    


# Create your models here.
