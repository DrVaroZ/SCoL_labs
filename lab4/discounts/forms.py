from django import forms


class DiscountApplyForm(forms.Form):
    code = forms.CharField()
