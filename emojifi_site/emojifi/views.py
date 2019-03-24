import json
import itertools
import emoji
from emojifi import dispatch_request
from emojifi import TYPE_TO_DISPATCH_FUNC
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


def emojifi_types(request: HttpRequest):
    return HttpResponse(
        json.dumps({
            'types': list(TYPE_TO_DISPATCH_FUNC.keys())
        }),
        content_type='application/json',
    )
