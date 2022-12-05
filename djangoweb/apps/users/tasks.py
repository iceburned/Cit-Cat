import logging
from time import sleep

from celery import shared_task
from django.db.models import Q


@shared_task
def search_in_subcategory(asd):
    sleep(3)
    # object_list = forum_subcategories.objects.filter(
    #     Q(title__icontains=query) & Q(category_id=cat_id))
    logging.info('search done!!')
    return
