from django.db import models


class TitleManager(models.Manager):
    def with_entry_counts(self):
        return self.annotate(models.Count('entries'))


class EntryManager(models.Manager):
    def submit_entry(self, title, entry):
        from eksiapp.models import Title
        title, created = Title.objects.get_or_create(title_text=title)
        return self.create(title=title, entry_text=entry)
