
from .models import Title, Entry

def get_title_info(title_id):
    t = Title.objects.get(title_id)
    return {
        "title": list(Title.objects.filter(pk=title_id).values()),
        "entries": list(Entry.objects.filter(title=title_id).values()),
        "num_of_entries": t.n_entries()}
