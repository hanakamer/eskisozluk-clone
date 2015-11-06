import json

from django.forms.models import model_to_dict
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count
from eksiapp.models import Title, Entry
from eksiapp.entry_creation import create_entry_with_title
from eksiapp.view_helpers import get_title_info


def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

def make_serializable(iterable):
    return [{str(k): v for k, v in item.iteritems()} for item in iterable]

def all_titles(request):
    titles =  Title.objects.annotate(Count('entries')).values()

    output_dict = make_serializable(titles)
    return JsonResponse(output_dict, safe=False)

def title(request, title_id):
    title = Title.objects.annotate(Count('entries')).get(pk=title_id)
    entries_dict = make_serializable(title.entries.values())

    output_dict = model_to_dict(title)
    output_dict['entries__count'] = title.entries__count
    output_dict['entries'] = entries_dict
    return JsonResponse(output_dict, safe=False)

@csrf_exempt
def submit_entry(request):
    if request.method == "POST":
        entry = request.POST['entry']
        title = request.POST['title']
        return JsonResponse({'id': create_entry_with_title(title, entry)})


def create_entry_with_title(title, entry):
    tmp_title,created = Title.objects.get_or_create(title_text=title)
    Entry.objects.create(entry_text=entry, title=tmp_title  )
    return tmp_title.id
