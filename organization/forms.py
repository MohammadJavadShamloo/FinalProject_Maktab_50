from django import forms


class ReportForm(forms.Form):
    """
    Form For Making report
    """
    report = forms.CharField(widget=forms.Textarea)
