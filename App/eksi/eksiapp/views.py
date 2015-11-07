import json

from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse

from eksiapp.models import Title, Entry


def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

def make_serializable(iterable):
    return [{str(k): v for k, v in item.iteritems()} for item in iterable]

def all_titles(request):
    titles =  Title.objects.with_entry_counts().values()

    output_dict = make_serializable(titles)
    return JsonResponse(output_dict, safe=False)

def title(request, title_id):
    title = Title.objects.with_entry_counts().get(pk=title_id)
    entries_dict = make_serializable(title.entries.values())

    output_dict = model_to_dict(title)
    output_dict['entries__count'] = title.entries__count
    output_dict['entries'] = entries_dict
    return JsonResponse(output_dict, safe=False)

@csrf_exempt
def submit_entry(request):
    if request.method == "POST":
        entry_text = request.POST['entry']
        title = request.POST['title']
        entry = Entry.objects.submit_entry(title, entry_text)

        return JsonResponse({'id': entry.id})
