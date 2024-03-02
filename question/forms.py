from django import forms
from .models import Question, Comment

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['summary', 'question', 'head_image']
        widgets = {
            'summary': forms.TextInput(
                attrs={
                    'class': 'form-control border-0',
                    'style': 'background-color: #80E12A; box-shadow: none; max-length: 30;',
                    'placeholder': 'write a title',
                }),
            'question': forms.Textarea(
                attrs={
                    'class': 'form-control border-0',
                    'style': 'background-color: #F2F2F2; box-shadow: none; border-color: #F2F2F2; min-height: 15; overflow-y: hidden; resize: none;',
                    'rows': 15,
                    'placeholder': 'write a content',
                    'onkeydown':'resize(this)',
                    'onKeyUp': 'resize(this)',
                }),
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': forms.TextInput(
                attrs={
                    'class': 'w-100 pt-1 pb-1 ps-3 pe-3 rounded-3 border border-2 border-dark',
                    'style': 'font-size: 20px; box-shadow: none;',
                    'placeholder': 'write a comment',
                }),
        }    