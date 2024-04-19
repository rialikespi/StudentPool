from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Question, Answer
from .forms import QuestionForm
from notes.models import Note

# Create your views here.

def home(response):
    return render(response, "index.html", {})

def display_combined_data(request, module_id = None):

    if 'quest' in request.GET:
        quest = request.GET['quest']
        questions = Question.objects.filter(title_icontains = quest).order_by('questionID')
    else:
        if module_id:
            questions = Question.objects.filter(moduleID = module_id).order_by('questionID')
        else:
            questions = Question.objects.all().order_by('questionID')

    '''if 'n' in response.GET:
        #note = response.GET['n']
        notes = Note.objects.all()
    else:
        if module_id:
            notes = Note.objects.filter(moduleID = module_id).order_by('note.pk')

        else:
            notes = Note.objects.all().order_by('note.pk')'''
    
    if 'note' in request.GET:
        note_query = request.GET['note']
        notes = Note.objects.filter(title__icontains=note_query).order_by('pk')
    else:
        if module_id:
            notes = Note.objects.filter(moduleID=module_id).order_by('pk')
        else:
            notes = Note.objects.all().order_by('pk')

    if 'ans' in request.GET:
        ans = request.GET['ans']
        answers = Answer.objects.filter(title_icontains = ans).order_by('questionID')
    else:
        answers = Answer.objects.all().order_by('questionID')

    #dashboard_view(response)
    
    return render(request, "module.html", { 'questions': questions, 'answers': answers, 'notes': notes})


def add_questions(response):
    if response.method == "POST":
        form = QuestionForm(response.POST or None)
        if form.is_valid():
            form.save()  
            messages.success("Question created")
            return redirect("module")
        else:
            messages.error("Question not added")
    else:
        form = QuestionForm()
    return render(response, "module.html", {"form" : form})

def dashboard_view(request):
    notes = Note.objects.all()  # Retrieves all notes, adjust the query as needed
    return render(request, 'module.html', {'notes': notes})

'''def add_asnwer(response):
    if response.method == "POST":
        form = AnswerForm'''

'''def dashboard(request):
    notes = Note.objects.all()
    notes = [{
        'id': note.id,
        'title': note.title,
        'average_rating': note.average_rating(),
    } for note in notes]
    return render(request, 'dashboard.html', {'notes': notes})'''







        




    

    
    



