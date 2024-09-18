from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings

# @receiver(post_save, sender=Profile)
def CreateProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )

        send_mail(
            "Welcome!",
            "Welcome to this App :D",
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )

        print(send_mail)

@receiver(post_save, sender=Profile)
def UpdateProfile(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()

def deleteUser(sender, instance, **kwargs):
    user = instance.user
    if user:
        user.delete()

post_save.connect(CreateProfile, sender=User)
post_delete.connect(deleteUser, sender=Profile)

# bug jika pake signals delete, saat hapus dari user akan error
# tapi saat hapus dari profile tidak

