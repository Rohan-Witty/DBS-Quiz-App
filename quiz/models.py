from operator import concat
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Question(models.Model):
    qid = models.IntegerField(primary_key= True)
    qstring = models.CharField(max_length=200)
    marks = models.IntegerField()
    def __str__(self):
        return self.qstring
    class Meta:
        db_table = "question"

class Option(models.Model):
    oid = models.IntegerField()
    ostring = models.CharField(max_length=200)
    qid = models.CharField(max_length=200)
    oc_id = models.IntegerField(primary_key=True)
    def __str__(self):
        return self.qstring
    class Meta:
        db_table = "option_choices"

class CorrectOption(models.Model):
    qid = models.IntegerField(primary_key=True)
    oid = models.IntegerField()
    def __str__(self):
        return self.qid
    class Meta:
        db_table = "correct_option"



# class Student(AbstractUser):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     id = models.CharField(max_length=13,primary_key=True)
#     name = models.CharField(max_length=100)
#     password = models.CharField(max_length=50)
#     def __str__(self):
#         return self.name
#     class Meta:
#         db_table = "student"
