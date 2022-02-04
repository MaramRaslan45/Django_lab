from django import forms
from .models import user

class userform(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=50)
    password = forms.CharField(max_length=20)
    cpassword = forms.CharField(max_length=20)

class updateform(forms.ModelForm):

    class Meta:
        model = user
        fields = '__all__'




