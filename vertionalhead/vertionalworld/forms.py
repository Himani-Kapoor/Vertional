from django import forms


class SumForm(forms.Form):
    a = forms.IntegerField(label='Number A', required=True)
    b = forms.IntegerField(label='Number B', required=True)
