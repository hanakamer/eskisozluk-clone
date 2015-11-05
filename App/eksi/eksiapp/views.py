import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Title, Entry
from .entry_creation import create_entry_with_title
from .view_helpers import get_title_info
from pprint import pprint

def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

def json_response(d):
    d = json.dumps(d, default=date_handler)
    return HttpResponse(d, content_type="application/json")


def all_titles(request):
    titles =  Title.objects.all()
    data = json.loads(serializers.serialize('json',titles))
    d={}
    d['results']=data
    d['num_of_entries']=get_num_of_entry()
    print(d)
    return json_response(d)

#
@csrf_exempt
def submit_entry(request):
    if request.method == "POST":
        entry = request.POST['entry']
        title = request.POST['title']
        return json_response({'id': create_entry_with_title(title, entry)})
#
#
#
def title(request,title_id):
    return json_response(get_title_info(title_id))
#
def get_num_of_entry():
    obj={}
    for i in Entry.objects.all():
        obj[str(i.title)]=len(list(Entry.objects.filter(title=i.title.id).values()))
    pprint(obj)
    return obj
#
def get_title_info(title_id):
    t = Title.objects.get(pk=title_id)
    return {
        "title": list(Title.objects.filter(pk=title_id).values()),
        "entries": list(Entry.objects.filter(title=title_id).values()),
        "num_of_entries": t.n_entries()}
def create_entry_with_title(title, entry):
    tmp_title,created = Title.objects.get_or_create(title_text=title)
    Entry.objects.create(entry_text=entry, title=tmp_title  )
    return tmp_title.id
