from django import forms
from app1.models import PrincipalMessage

class PrincipalMessageForm(forms.ModelForm):
    class Meta:
        model = PrincipalMessage
        fields = ['name', 'email', 'subject', 'message']