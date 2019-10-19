from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name 
    
    class Meta:
        db_table = 'at_students'

class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " "
    
    class Meta:
        db_table = 'at_teachers'