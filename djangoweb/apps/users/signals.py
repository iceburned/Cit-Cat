from django.db.models import signals
from django.db.models import signals
from django.dispatch import receiver

from djangoweb.apps.users.models import AboutData
from djangoweb.services.ses import SESServiceAbout


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
