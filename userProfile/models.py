from django.db import models
from django.contrib.auth.models import User
#import modules from here

from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #password = password saved in user creation form

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    user_email = models.CharField(max_length=255)
    
    def getUserPassword(self):
        return self.user.password

    user_type = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='media', default='default.png')

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs) :
        if created:
            Profile.objects.create(user = instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs) :
        instance.profile.save