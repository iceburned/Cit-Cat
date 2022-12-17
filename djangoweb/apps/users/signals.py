from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db.models import signals
from django.dispatch import receiver

from djangoweb.apps.users.models import AppUser, AboutData

from django.core.exceptions import ObjectDoesNotExist

from djangoweb.services.ses import SESServiceAbout, SESServiceAppUser


@receiver(signals.post_save, sender=AboutData)
def handle_message_created(sender, instance, created, **kwargs):
    if created:
        asking_admin = AboutData.objects.last()

        SESServiceAbout().send_email(asking_admin)
        print("Message send")


# @receiver(signals.post_save, sender=AppUser)
# def handle_message_created(sender, instance, created, **kwargs):
#     if created:
#         last_user = AppUser.objects.last()
#         last_user_email = last_user.email
#         SESServiceAppUser().send_email(last_user_email)
#         print("Message send")
