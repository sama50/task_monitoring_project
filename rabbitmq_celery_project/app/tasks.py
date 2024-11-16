from celery import shared_task
import time
@shared_task
def celery_task():
    time.sleep(10)
    print("hey..........................")