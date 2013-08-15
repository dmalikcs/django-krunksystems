from django.contrib import admin 
from .models import TrainingCourse,CorporateTraining,AcademyTraining,IndustrialTraining

admin.site.register(TrainingCourse)
admin.site.register(CorporateTraining)
admin.site.register(AcademyTraining)
admin.site.register(IndustrialTraining)
