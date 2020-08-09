from django import forms

class LogForm(forms.Form):
    url_type = forms.IntegerField()
    cookie = forms.CharField(max_length = 2000)
    start = forms.IntegerField()
    end = forms.IntegerField()