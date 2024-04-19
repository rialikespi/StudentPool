from django.shortcuts import render, redirect, HttpResponse, get_object_or_404 #unsure if redirect is needed
from django.contrib import messages
from .forms import NoteForm, ReviewForm  
from .models import Note, Review
from django.http import HttpResponseNotFound, HttpResponseNotAllowed, FileResponse
from django.template import engines
from django.db.models import Avg, Count

# Create your views here.
# different views or routes to access on website

def home(request):
    return render(request, 'home.html')

def page(request):
    return render(request, 'oldnotespage.html')

def upload_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user  # assuming you have user authentication
            note.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm()
    return render(request, 'upload_note.html', {'form': form})

def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    reviews = Review.objects.filter(note=note)
    rating_data = reviews.aggregate(average_rating=Avg('rating'), count_reviews=Count('id'))
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.note = note
            review.user = request.user
            review.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = ReviewForm()

    return render(request, 'notespage.html', {
        'note': note,
        'reviews': reviews,
        'average_rating': rating_data['average_rating'],
        'count_reviews': rating_data['count_reviews'],
        'form': form
    })


def average_rating(self):
        reviews = self.reviews.all()
        if reviews:
            return sum([review.rating for review in reviews]) / len(reviews)
        return 0

'''def delete_note(request, note_id):
    if request.method == 'DELETE':
        note = get_object_or_404(Note, pk=note_id) # fetch note or 404 if note doesn't exist
        note.delete()
        messages.success(request, 'Note deleted successfully!')
        return HttpResponse(status=204)
    else:
        return HttpResponseNotAllowed(['DELETE'])

def get_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id) # fetch note or 404 if note doesn't exist
    return render(request, 'notes.html', {'note': note}) '''

'''def upload_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            messages.success(request, 'Note uploaded successfully!')
            return redirect('page')
        else:
            messages.error(request, 'Error uploading note. Please check the form.')
    else:
        form = NoteForm()
    return render(request, 'upload_note.html', {'form': form})

def download_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    filename = note.upload.path
    response = FileResponse(open(filename, 'rb'))
    return response'''

'''def note_detail(request, pk):
    note = Note.objects.get(pk=pk)
    reviews = note.reviews.all()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.note = note
            review.user = request.user  # assuming you have user authentication
            review.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = ReviewForm()
    return render(request, 'oldnotespage.html', {'note': note, 'reviews': reviews, 'form': form})'''