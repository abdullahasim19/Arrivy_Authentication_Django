from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def test(request):
    return HttpResponse('Hello World')


def create_task(data):
    entity_ids = []
    entity_ids = list(data.get('entity_ids'))

    resource_ids = data.get('resource_ids')

    
