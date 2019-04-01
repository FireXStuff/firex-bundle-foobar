from firexapp.engine.celery import app
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


@app.task(returns=("success",))
def foo(define_success="success!!!"):
    logger.debug(define_success)
    return define_success


@app.task(returns=("defeat",))
def bar(success):
    return "No " + success
