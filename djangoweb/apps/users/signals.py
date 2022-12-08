from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db.models import signals
from django.dispatch import receiver

from djangoweb.apps.users.models import AppUser


@receiver(signals.post_save, sender=AppUser)
def handle_user_created(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(id=2)
        group.user_set.add(instance)
        print(group)
