from tkinter.ttk import Style
from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['dish_name', 'ingredient', 'recipe', 'head_image']
        widgets = {
            'dish_name': forms.TextInput(
                attrs={
                    'class': 'form-control border-0',
                    'style': 'background-color: #80E12A; box-shadow: none; max-length: 30;',
                    'placeholder': 'write a title',
                }),
            'ingredient': forms.Textarea(
                attrs={
                    'class': 'form-control border-0',
                    'style': 'box-shadow: none;',
                    'cols': 95,
                    'rows': 5,
                    'placeholder': 'write ingredients',
                }),
            'recipe': forms.Textarea(
                attrs={
                    'class': 'form-control border-0',
                    'style': 'background-color: #F2F2F2; border-color: #F2F2F2; box-shadow: none; min-height: 15; overflow-y: hidden; resize: none;',
                    'rows': 15,
                    'placeholder': 'write your recipe',
                    'onkeydown':'resize(this)',
                    'onKeyUp': 'resize(this)',
                }),    
        }
