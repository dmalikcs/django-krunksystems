from django.db import models
from django import forms

rating=(
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
        )


class feedback(models.Model):
    name=models.CharField(verbose_name='Name',
            max_length=75,
            )
    email=models.EmailField(verbose_name='Email',
            )
    website=models.URLField(verbose_name='Website',
            )
    jobportal=models.CharField(verbose_name='Job Portal',
            max_length=30,
            choices=(('Odesk','Odesk'),('elance','elance'),)
            )
    budget=models.CharField(verbose_name='Budget',
            max_length=2,
            choices=rating,
            )
    experience=models.CharField(verbose_name='Expr',
            max_length=2,
            choices=rating,
            )
    portfolio=models.CharField(verbose_name='Portfolio',
            max_length=3,
            choices=rating,
            )
    suggestion=models.TextField(verbose_name='Suggestion',
            max_length=200,
            )
    class Meta:
        verbose_name='Feedback'
        verbose_name_plural='feedbacks'
    def __unicode__(self):
        return self.name


class feedbackModelForm(forms.ModelForm):
    budget=forms.ChoiceField(choices=rating,
            #widget=forms.RadioSelect()
            )
    experience=forms.ChoiceField(choices=rating,
            #widget=forms.RadioSelect()
            )
    portfolio=forms.ChoiceField(choices=rating,
            #widget=forms.RadioSelect()
            )
    class Meta:
        model=feedback
        fields=['name','email','website','budget','experience','portfolio','jobportal','suggestion']
