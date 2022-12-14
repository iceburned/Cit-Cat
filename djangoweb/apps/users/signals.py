from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db.models import signals
from django.dispatch import receiver

from djangoweb.apps.users.models import AppUser, AboutData

from django.core.exceptions import ObjectDoesNotExist


# @receiver(signals.post_save, sender=AppUser)
# def handle_user_created(sender, instance, created, **kwargs):
#     a = 1
#     if created and instance.is_superuser:
#         pass
#     else:
#         try:
#             group = Group.objects.get(id=2)
#             group.user_set.add(instance)
#         except ObjectDoesNotExist:
#             raise (f"Need to create 3 groups to not see this error\n"
#                 f"--------------------------\n"
#                 f"first group should be 'admins'\n"
#                 f"second one 'users'\n"
#                 f"and third one 'mods'\n"
#                 f"--------------------------\n"
#                 f"This is needed, because when user register, he/she is added automaticly to group 2\n"
#                 f"which is regular user!")


@receiver(signals.post_save, sender=AboutData)
def handle_message_created(sender, instance, created, **kwargs):
    if created:
        print("Message send")