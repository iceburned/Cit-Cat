
import logging


from celery import shared_task


from djangoweb.apps.utils.cat_pics import main_cat


@shared_task
def search_in_cat_api():
    cat_link = main_cat()
    logging.info('search done!!')
    return cat_link
