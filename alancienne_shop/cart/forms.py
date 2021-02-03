from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 31)]


class CartAddProductForm(forms.Form):
    # def __init__(self,maxStock):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,
                                      coerce=int)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
