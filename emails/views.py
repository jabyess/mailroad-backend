from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Email, Author
import datetime

# Create your views here.
test = {"sup": "test"}


def index(request):
    return JsonResponse(test)


def create_email(request):
    date = datetime.datetime.now()
    e = Email(body="testing text", created_at=date, updated_at=date)
    auth = Author(id=1, emails=e)
    print(auth)
    return HttpResponse('sup')
