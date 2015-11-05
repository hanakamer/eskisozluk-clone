from .models import Title, Entry

def create_entry_with_title(title, entry):
    tmp_title,created = Title.objects.get_or_create(title_text=title)
    Entry.objects.create(entry_text=entry, title=tmp_title  )
    return tmp_title.id
