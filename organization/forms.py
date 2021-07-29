from django import forms


class ReportForm(forms.Form):
    report = forms.CharField(widget=forms.Textarea)
