from django import forms

class StudentCred(forms.Form):
    index_number = forms.CharField(
        max_length = 12,
        strip = True,
        label = "Index Number"
    )

    student_key = forms.CharField(
        label = "Key"
    )
