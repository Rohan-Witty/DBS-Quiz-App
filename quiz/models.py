from operator import concat
from django.db import models

# Create your models here.

class Question(models.Model):
    qid = models.IntegerField(primary_key= True)
    qstring = models.CharField(max_length=200)
    marks = models.IntegerField()
    def __str__(self):
        return self.qid
    class Meta:
        db_table = "question"

class Option(models.Model):
    oid = models.IntegerField()
    ostring = models.CharField(max_length=200)
    # qid = models.ForeignKey(Question, on_delete=models.CASCADE, db_column="qid")
    qid = models.CharField(max_length=200)
    oc_id = models.IntegerField(primary_key=True)
    def __str__(self):
        return self.qstring
    class Meta:
        db_table = "option_choices"

