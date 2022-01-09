
from django.urls import path, include
from rest_framework import routers
from .import views
# from rest_framework_swagger.views import get_swagger_view
# from rest_framework.schemas import get_schema_view

app_name='student_api'

# schema_view = get_swagger_view(title='Student API')
#
router = routers.DefaultRouter()
router.register(r'student',views.StudentDetailsViewSet)
router.register(r'course', views.CourseViewSet)
router.register(r'subjects',views.SubjectsViewSet)
router.register(r'teachers', views.TeachersViewSet)
router.register(r'marks', views.MarksViewSet)


urlpatterns=[
           path('', include(router.urls)),
           # path('student',schema_view),
           path('marks', views.MarksView.as_view(), name='marks'),
           path('student',views.StudentView.as_view(), name='student_details')
           path('student_details',views.StudentDetailsView, name='student_info'),
           path('teacherslist', views.ListCreateTeacher.as_view(), name='teacherlist'),
#            path('auth',include('rest_framework.urls'), name='rest_framework'),

]



