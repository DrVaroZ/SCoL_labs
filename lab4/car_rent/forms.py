from django import forms
from .models import Car, Review


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'car_model', 'release_year', 'cost', 'rent_per_day', 'image']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['mark', 'text']
