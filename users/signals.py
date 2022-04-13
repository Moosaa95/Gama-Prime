# add signals
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """  

        create profile automatically when user is created

    Args:
        sender (type):  sender
        instance (type):  instance
        created (type):  created
        **kwargs (type):  **kwargs
    """
    if created:
        Profile.objects.create(user=instance)


# save profile automatically when user is saved
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """  

        save profile automatically when user is saved

    Args:
        sender (type):  sender
        instance (type):  instance
        **kwargs (type):  **kwargs
    """
    instance.profile.save() # save profile
    