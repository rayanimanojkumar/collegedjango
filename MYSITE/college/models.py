from django.db import models

# Create your models here.
class StudentDetails(models.Model):
    student = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    mobile_no = models.CharField(max_length=10)
    email_id = models.EmailField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name



class Course(models.Model):
    course = models.IntegerField(primary_key=True)
    course_name = models.CharField(max_length=30)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    def __str__(self):
        return self.course_name

class Subjects(models.Model):
    student = models.ForeignKey(StudentDetails,on_delete=models.CASCADE)
    subject = models.IntegerField(primary_key=True)
    subject_name = models.CharField(max_length=30)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return self.subject_name

class Teachers(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    subject = models.ForeignKey(Subjects,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    email_id = models.EmailField()
    mobile_no = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name

class Marks(models.Model):
    student = models.ForeignKey(StudentDetails,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects,on_delete=models.CASCADE)
    sem_marks = models.IntegerField()
    internal_marks = models.IntegerField()
    total_marks = models.IntegerField()

    def __str__(self):
        return self.student

