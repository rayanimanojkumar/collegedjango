
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status


# STUDENT_URL = reverse('student_api:marks')
USER_URL = reverse('student_api:auth')
class StudentsDetailsTestCase(APITestCase):

    def test_login_user(self):
        self.assertTrue(self.client.login(username='manoj', password='abc123'))
        response = self.client.get(USER_URL)
        self.assertEqual(response.status_code,status.HTTP_200_OK)



#    def test_details(self):
    #     response = self.client.get(STUDENT_URL, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)






















# from django.test import TestCase
# from django.db import connection


# from .models import Course
# def test_custom_query(self):
#
# class ModelTests(TestCase):
#      def setUp(self):
#          self.course1= Course.objects.create(course=2809, course_name='MECH', start_date='2021-09-23', end_date='2022-09-24')
#
#      def test_course(self):
#          course1=Course.objects.get(course_name='MECH')
#          self.assertEqual(course1.course_name, 'MECH')
# from django.test import TestCase
# from django.db import connection
# class course_Test(TestCase):
#     def test_first(self):
#         cursor = connection.cursor()
#         try:
#             cursor.execute('select student_id,subject_id, sem_marks, internal_marks, max(total_marks) as h_marks from collegedetails.college_marks;')
#             cursor.fetchone()
#         finally:
#             cursor.close()

# from django.test import TestCase
# from .models import *
# from rest_framework import reverse
# from rest_framework import status
# class StudentsDetailsViewTest(TestCase):
#     def test_query_search(self):
#         query_set = StudentDetails.objects.raw('SELECT * FROM collegedetails.college_studentdetails LIMIT 3;')
#         url = (reverse('Student_Details', args=(query_set)))
#         response=self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)


