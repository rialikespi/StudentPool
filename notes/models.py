from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey relationship with the User model
    file = models.FileField(upload_to='notes/')  # FileField to store the PDF file
    
    '''def average_rating(self):
        ratings = self.rating_set.all()
        if ratings:
            return sum(rating.value for rating in ratings) / len(ratings)
        return 0'''

    def __str__(self):
        return self.title
    
class Review(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField() # store stars
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return f"{self.title} by {self.user.username}"

'''class ReviewRating(models.Model):
    note = models.ForeignKey('Note', related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True) # is empty
    rating = models.FloatField() # to store half stars
    ip = models.CharField(max_length=20, blank=True)
    #status = models.BooleanField=True
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject'''