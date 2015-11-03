from django import forms

class TestForm(forms.Form):
    test_label = forms.CharField(label='Nome do Teste', max_length=100)
    test_url = forms.CharField(label='url', max_length=1000)
