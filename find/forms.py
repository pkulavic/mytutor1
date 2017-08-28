from django import forms
from tutorprofile.models import TutorProfile

class FindForm(forms.ModelForm):
    class Meta:
        model = TutorProfile
        fields = [
            'subject',
            'city'
        ]



class PaymentForm(forms.Form):
    parent_name = forms.CharField(max_length=120)
    student_name = forms.CharField(max_length=120)
    tutor = forms.CharField(max_length=120)
    time = forms.CharField(max_length=120)
