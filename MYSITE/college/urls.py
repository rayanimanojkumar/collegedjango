
from django.urls import path, include
from rest_framework import routers
from .import views
# from rest_framework_swagger.views import get_swagger_view
# from rest_framework.schemas import get_schema_view



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


]



