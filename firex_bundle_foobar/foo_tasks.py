from firexapp.engine.celery import app
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


@app.task
def foo(define_success="success!!!"):
    logger.debug(define_success)
