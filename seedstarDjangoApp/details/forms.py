from django import forms
from details.models import Details as details
class Details(forms.ModelForm):
    name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = details
        fields = ('name', 'email',)