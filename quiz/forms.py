from django import forms
from django.forms import ModelForm
from .models import Question, Option, CorrectOption, Assign
from django.db import connection
    
class Quiz(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super(Quiz, self).__init__(*args, **kwargs)
        for question in questions:
            qid = question['question'].qid
            self.fields['qid_' + str(qid)] = forms.ChoiceField(choices=[(option.oid, option.ostring) for option in question['options']], widget=forms.RadioSelect)
    
    def save(self, user_id):
        for key, value in self.items():
            if key.startswith('qid_'):
                qid = key.split('_')[1]
                option = Option.objects.get(qid=qid, oid=value)
                print([user_id, qid, option.oid])
                with connection.cursor() as cursor:
                    cursor.callproc('update_assign', [user_id, qid, option.oid])
        return True