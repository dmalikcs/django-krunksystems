from django.db import models
from django import forms

class A2M1_contactus(models.Model):
    name=models.CharField(
            verbose_name="Your name",
            max_length=50,
            unique=False,
            null=False,
            error_messages={'required': 'Please enter your name'},
#            help_text="Kindly enter the First Name"
            )
    mobile=models.CharField(
            verbose_name='Mobile/Skpye',
            max_length='15',
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
        return self.name
    class Meta:
        verbose_name='Query'
        verbose_name_plural='Queries'

                                
class A2F1_contactus(forms.ModelForm):
    '''Contact form with extra widget
       Twitter-bootstrap class added
    '''
    class Meta:
        model=A2M1_contactus
        fields=('name','mobile','Email','Message',)
        widgets={
                'name':forms.TextInput(
                    attrs={
                        'class':'input-xlarge',
                        'placeholder':'Your Name',
                        },
                    ),
                'mobile':forms.TextInput(
                    attrs={
                        'class':'input-xlarge',
                        'placeholder':'What is your mobile ?',
                        }),
                'Email':forms.TextInput(
                    attrs={
                        'class':'input-xlarge',
                        'placeholder':'What is your email ?',
                        }),
                'Message':forms.Textarea(
                    attrs={
                        'class':'input-xlarge',
                        'placeholder':'What do you have in your mind ?',
                        }),
                }

