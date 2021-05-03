from config import celery_app

#celery tasks
# 1: to process sales 
# 2: move files to archive

@celery_app.task()
def process_sale():
    """ Task to process sales"""
    pass


