from django.contrib.auth import get_user_model
from django.db.models import signals
from django.dispatch import receiver

created_user = get_user_model


@receiver(signals.post_save, sender=created_user)
def send_mail(*args, **kwargs):
    pass