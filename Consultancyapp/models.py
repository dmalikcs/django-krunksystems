from django.db import models

python_categories=(
        ('Django','dj'),
        ('OpenERP','dj'),
        )

django_categories=(
        ('Django','dj'),
        ('OpenERP','dj'),
        )

opensource_categories=(
        ('Django','dj'),
        ('OpenERP','dj'),
        )

midrange_categories=(
        ('Django','dj'),
        ('OpenERP','dj'),
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



