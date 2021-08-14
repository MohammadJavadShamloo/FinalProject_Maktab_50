from django import forms
from django.forms import inlineformset_factory

from inventory.models import Product
from quote.models import QuoteItem, Quote


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['organization', ]


class QuoteItemForm(forms.ModelForm):
    class Meta:
        model = QuoteItem
        fields = ['product', 'count_of_product', 'off_percent', ]


QuoteItemFormSet = inlineformset_factory(Quote,
                                         QuoteItem,
                                         form=QuoteItemForm,
                                         extra=Product.objects.count(),
                                         max_num=100)
