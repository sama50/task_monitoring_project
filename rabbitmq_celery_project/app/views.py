from django.shortcuts import HttpResponse
from .tasks import celery_task
# Create your views here.


def home(request):
    celery_task.delay()
    return HttpResponse("Done")
