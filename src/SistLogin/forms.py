from django import forms

class LoginForm(forms.Form):
    username = forms.EmailField(label='Your email', max_length=300)
    passwd = forms.CharField()