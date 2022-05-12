# project/tasks/sample_tasks.py

import time

from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task
def create_task(task_type):
    logger.info('Creating a task')
    time.sleep(int(task_type) * 10)
    return True
