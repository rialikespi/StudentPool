from django import forms
from .models import Question, Module, Answer

class QuestionForm(forms.ModelForm):
    class meta:
        model = Question
        fields = ['questionID', 'moduleID', 'userID', 'title', 'text', 'is_favourite']

'''class NotesForm(forms.ModelForm):
    class meta:
        model = Notes
        fields = ['noteID', 'userID', 'moduleID', 'text']'''

class ModuleForm(forms.ModelForm):
    class meta:
        model = Module
        fields = ['moduleID', 'title', 'factulty']

class AnswerForm(forms.ModelForm):
    class meta:
        model = Answer
        fields = ['answerID', 'questionID', 'userID', 'text']
