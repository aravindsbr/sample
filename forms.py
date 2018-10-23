from django import forms

class InputForm(forms.Form):
    input_1 = forms.CharField(max_length = 100)
    input_2 = forms.CharField(max_length = 100)
