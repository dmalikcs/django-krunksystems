from django.db import models
from django import forms

class A2M1_contactus(models.Model):
    First_name=models.CharField(
            verbose_name="First name",
            max_length=50,
            unique=False,
            null=False,
            error_messages={
                'required':'Kindly enter the first name',
                'max_length':'Please enter first name below 50 char',
                'min_length':'Kindly provide min charter',

                }
#            help_text="Kindly enter the First Name"
            )
    Last_name=models.CharField(
            verbose_name="Last name",
            max_length=20,
            unique=False,
            null=False,
            blank=False,
            error_messages={
                'required':'Kindly enter the first name',
                }
 #           help_text="Kindly enter the last name",
            )
    Email=models.EmailField(
            verbose_name='Email',
            null=True, 
            blank=False, 
  #          help_text='Kindly eneter the correct email id',
            )
    Message=models.TextField(
            verbose_name='message',
            null=False, 
            blank=False,
   #         help_text='Kindly enter the message'

            )
    requested_date=models.DateTimeField(
            auto_now_add=True,
            )
    last_response_date=models.DateTimeField(
            auto_now=True
            )
    def __unicode__(self):
        return u'%s %s' % (self.First_name,self.Last_name)

                                
class A2F1_contactus(forms.ModelForm):
    class Meta:
        model=A2M1_contactus
