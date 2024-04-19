# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
# Create your models here.

class User(models.Model):
    userID = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length = 255, blank = True)
    last_name = models.CharField(max_length = 255, blank = True)
    user_email = models.EmailField()
    password_hash = models.CharField(max_length = 255, blank = True)
    user_type = models.CharField(max_length = 255, blank = True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Module(models.Model):
    moduleID = models.CharField(max_length = 20)
    title = models.CharField(max_length = 255)
    faculty = models.CharField(max_length = 255)

    def __str__(self):
        return f"{self.moduleID} {self.title}"
    
class User_Module(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name= 'user_modules')
    module_code = models.ForeignKey(Module, on_delete = models.CASCADE, related_name = 'module_users')

    def __str__(self):
        return f"{self.user} {self.module_code}"
    

class Question(models.Model):
    questionID = models.AutoField(primary_key = True)
    moduleID = models.ForeignKey(Module, on_delete = models.CASCADE, related_name='module_question')
    userID = models.ForeignKey(User, on_delete = models.CASCADE, related_name='user_question')
    title = models.CharField(max_length = 255)
    text = models.CharField(max_length = 255)
    add_time = models.DateTimeField(auto_now_add=True)
    is_favourite = models.BooleanField()

    def __str__(self):
        return self.title
  
    
class Answer(models.Model):
    answerID = models.AutoField(primary_key = True)
    questionID = models.ForeignKey(Question, on_delete = models.CASCADE, related_name='question_answer')
    userID = models.ForeignKey(User, on_delete = models.CASCADE, related_name='user_answer')
    title = models.CharField(max_length = 255)
    text = models.CharField(max_length = 255)

    def __str__(self):
        return self.title
    
    
class Notes(models.Model):
    noteID = models.AutoField(primary_key = True)
    userID = models.ForeignKey(User, on_delete = models.CASCADE, related_name='user_notes')
    moduleID = models.ForeignKey(Module , on_delete = models.CASCADE, related_name='module_notes')
    title = models.CharField(max_length = 255)
    text = models.TextField()

    def __str__(self):
        return self.title
    
    
'''class Rating(models.Model):
    ratingID = models.AutoField(primary_key = True)
    slug = models.SlugField(max_length = 400, unique = True, blank = True)
    userID = models.ForeignKey(User, on_delete = models.CASCADE, related_name='user_rating')
    moduleID = models.ForeignKey(Module, on_delete = models.CASCADE, related_name='module_rating')
    questionID = models.ForeignKey(Question, on_delete = models.CASCADE, related_name='question_rating')
    answerID = models.ForeignKey(Answer, on_delete = models.CASCADE, related_name='answer_rating')
    ratingType = models.CharField(max_length = 50)

    def __str__(self):
        return f"{self.ratingID} {self.ratingType}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.ratingType)
        super(Rating, self).save(*args, **kwargs)'''