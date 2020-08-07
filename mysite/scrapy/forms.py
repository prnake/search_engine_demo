from django import forms

class LogForm(forms.Form):
    url = forms.CharField(max_length=2000)
    cookie = forms.CharField(max_length = 2000)
    start = forms.IntegerField()
    end = forms.IntegerField()