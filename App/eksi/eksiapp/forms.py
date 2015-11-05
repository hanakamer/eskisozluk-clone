from django import forms

class EntryForm(forms.Form):
    title = forms.Charfield(label='title', max_length=300)
    entry = forms.Charfiel(label=)
