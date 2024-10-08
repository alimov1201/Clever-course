from django import forms

from blog.models import Contact, Upcoming_event, Comment
from django.utils import timezone


class EventForm(forms.ModelForm):
    class Meta:
        model = Upcoming_event
        fields = ['event_datetime']
    
    def clean_event_datetime(self):
        event_datetime = self.cleaned_data.get('event_datetime')
        if event_datetime <= timezone.now():
            raise forms.ValidationError("The datetime must be in the future.")
        return event_datetime

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your message'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
                'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your message'}),
            }