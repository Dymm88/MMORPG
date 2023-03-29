from django import forms
from .models import Announcement, Review


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['author', 'header', 'category', 'content']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']
