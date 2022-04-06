from tkinter.messagebox import QUESTION
from django.db import models

# Create your models here.
class Exam(models.Model):
    qstring = models.CharField(max_length=200)
    oid = models.IntegerField()
    ostring = models.CharField(max_length=200)
    def __str__(self):
        return self.qstring
    class Meta:
        db_table = "AssignedQuestions"

