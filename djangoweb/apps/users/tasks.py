import logging
from time import sleep

from celery import shared_task


@shared_task
def search_in_subcategory(asd):
    sleep(3)
    logging.info('search done!!')
    return
