from django import forms


class StudentRegistration(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    discription = forms.CharField(widget=forms.Textarea)