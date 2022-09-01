from django import forms
from .models import Flashcard, Subject

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('subject',)

class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ('question', 'answer',)
