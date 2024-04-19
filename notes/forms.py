from django import forms
from .models import Note, Review
from django.db import models
from django.contrib.auth.models import User

class NoteForm(forms.ModelForm):
    class Meta: #inner class used to provide metadata about the form
        model = Note
        fields = ['title', 'content', 'file'] 

    def clean_file(self):
        file = self.cleaned_data.get('file', False)
        if file:
            if file.content_type != 'application/pdf':
                raise forms.ValidationError('Only PDF files are allowed.')
            if file.size > 5*1024*1024:  # Limit file size to 5MB
                raise forms.ValidationError('File size must be under 5MB.')
            return file
        else:
            raise forms.ValidationError("Couldn't read uploaded file")

class ReviewForm(forms.ModelForm):
     class Meta:
          model = Review
          fields = ['rating', 'title', 'content']

'''class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    upload = models.FileField(upload_to='notes/')
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    reviews = models.TextField(blank=True)'''