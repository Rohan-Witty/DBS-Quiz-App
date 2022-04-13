from django import forms
from django.db import connection


class Quiz(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop("questions")
        super(Quiz, self).__init__(*args, **kwargs)
        for i, question in enumerate(questions):
            self.fields[
                "Q" + str(i + 1) + ") " + question["question"].qstring
            ] = forms.ChoiceField(
                choices=[
                    (option.oid, option.ostring) for option in question["options"]
                ],
                widget=forms.RadioSelect,
                required=False,
            )

    def save(self, user_id, questions):
        """
        Writes the answers of the user to the database using the MySQL procedure `update_assign`
        """
        for i, (_, oid) in enumerate(self.cleaned_data.items()):
            qid = questions[i]["question"].qid
            if oid:
                with connection.cursor() as cursor:
                    cursor.callproc("update_assign", [user_id, qid, oid])
        return True
