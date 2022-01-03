# from django.test import TestCase
# from .models import StudentDetails
#
# class StudentTestCase(TestCase):
#     def setUp(self):
#         StudentDetails.objects.create(student=107,first_name='Sarath',last_name='R',mobile_no='8296431790',
#                                       email_id='sarath2gmail.com',address='Guntur, India')
#     def test_studentdetails_info(self):
#         qs=StudentDetails.objects.all()
#         self.assertEqual(qs.count(), 1)
# from django.db import connection
# def test_sql(self):
#
#        cursor = connection.cursor()
#        cursor.execute("select first_name,last_name from studentdetails ")
#        cursor.fetchall()

