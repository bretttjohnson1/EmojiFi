import json
import itertools
import emoji
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from django.http import response
from django.http import HttpRequest


def index(request: HttpRequest):
    return render(request, 'emojifi/main.html')


@csrf_exempt
def clapifi(request: HttpRequest):
    if request.method == 'POST':
        print(request.body.decode('utf-8'))
        original_text: str = json.loads(request.body.decode('utf-8'))['text']
        word_list = original_text.split(' ')
        return HttpResponse(
            json.dumps({
                'text': emoji.emojize(' :clap: ', use_aliases=True).join(word_list)
            }),
            content_type='application/json',
        )
    return HttpResponse(status=403)
