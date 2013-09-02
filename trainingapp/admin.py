from django.contrib import admin 
from .models import TrainingCourse,CorporateTraining,AcademyTraining,IndustrialTraining,TrainingSuccess,CourseOutline,MentorDetail,WhyThisTraining

admin.site.register(TrainingCourse)
admin.site.register(CorporateTraining)
admin.site.register(AcademyTraining)
admin.site.register(IndustrialTraining)
admin.site.register(TrainingSuccess)
admin.site.register(CourseOutline)
admin.site.register(MentorDetail)
admin.site.register(WhyThisTraining)
