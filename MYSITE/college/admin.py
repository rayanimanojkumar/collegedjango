from django.contrib import admin
from .models import StudentDetails,Course,Subjects,Teachers,Marks
# Register your models here.
admin.site.register(StudentDetails)
admin.site.register(Course)
admin.site.register(Subjects)
admin.site.register(Teachers)
admin.site.register(Marks)