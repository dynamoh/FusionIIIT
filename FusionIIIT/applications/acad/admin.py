from django.contrib import admin
from .models import BtechCurriculum,Course,BatchSemester,CurriculumCourse,CurriculumInstructor,MtechCurriculum,MtechSemester,Student_acad,Register,StudentRegistrationCheck,InitialRegistrations,FinalRegistrations
# Register your models here.

admin.site.register(BtechCurriculum)
admin.site.register(BatchSemester)
admin.site.register(Course)
admin.site.register(CurriculumCourse)
admin.site.register(CurriculumInstructor)
admin.site.register(MtechSemester)
admin.site.register(MtechCurriculum)
admin.site.register(Student_acad)
admin.site.register(Register)
admin.site.register(StudentRegistrationCheck)
admin.site.register(InitialRegistrations)
admin.site.register(FinalRegistrations)
