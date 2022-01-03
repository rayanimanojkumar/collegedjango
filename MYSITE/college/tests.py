# from django.test import TestCase
# from django.db import connection
#
# # Create your tests here.
#
from .models import Course
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

from rest_framework.test import APITestCase
