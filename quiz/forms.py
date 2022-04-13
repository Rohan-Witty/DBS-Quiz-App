from django import forms
from django.db import connection


class Quiz(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop("questions")
        super(Quiz, self).__init__(*args, **kwargs)
        for question in questions:
            qid = question["question"].qid
            self.fields["qid_" + str(qid)] = forms.ChoiceField(
                choices=[
                    (option.oid, option.ostring) for option in question["options"]
                ],
                widget=forms.RadioSelect,
                required=False,
            )

    def save(self, user_id):
        """ "
        Writes the answers of the user to the database using the MySQL procedure `update_assign`
        """
        for key, value in self.cleaned_data.items():
            if key.startswith("qid_"):
                qid = key.split("_")[1]
                if value != "":
                    with connection.cursor() as cursor:
                        cursor.callproc("update_assign", [user_id, qid, value])
        return True
