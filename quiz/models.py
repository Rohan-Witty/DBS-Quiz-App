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
        return self.ostring
    class Meta:
        db_table = "option_choices"

class CorrectOption(models.Model):
    qid = models.IntegerField(primary_key=True)
    oid = models.IntegerField()
    def __str__(self):
        return self.qid
    class Meta:
        db_table = "correct_option"

# assign questions to users
class Assign(models.Model):
    ac_id = models.IntegerField(primary_key=True)
    id = models.CharField(max_length = 13)
    qid = models.IntegerField()
    attempted_option = models.IntegerField()
    def __str__(self):
        return str(self.ac_id)
    class Meta:
        db_table = "assign"
