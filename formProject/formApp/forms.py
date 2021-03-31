from django import forms
class studentRegistration(forms.Form):
    sname=forms.CharField()
    sid=forms.IntegerField()
    sadd=forms.CharField()
