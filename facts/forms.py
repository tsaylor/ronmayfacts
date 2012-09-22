from django import forms

class NewFactForm(forms.Form):
    name = forms.CharField(max_length="50")
    email = forms.EmailField()
    factoid = forms.CharField()
