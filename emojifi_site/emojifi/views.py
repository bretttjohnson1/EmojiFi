import json
import itertools
import emoji
from .dispatcher.dispatcher import dispatch_request
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from django.http import response
from django.http import HttpRequest


def index(request: HttpRequest):
    return render(request, 'emojifi/main.html')


@csrf_exempt
def emojifi(request: HttpRequest):
    if request.method == 'POST':
        return HttpResponse(
            json.dumps({
                'text': dispatch_request(request)
            }),
            content_type='application/json',
        )
    return HttpResponse(status=403)
