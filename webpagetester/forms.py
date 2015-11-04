from django import forms

from webpagetester.models import Application

class TestForm(forms.Form):

    apps_list = Application.objects.all()
    select_options = []
    for app in apps_list:
        select_options.append((app.id, app.name))

    test_application = forms.ChoiceField(widget = forms.Select(),
                     choices =select_options, required = True, label='Aplicação')
    test_label = forms.CharField(label='Nome do Teste', max_length=100)
    test_url = forms.CharField(label='url', max_length=1000)

