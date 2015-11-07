from django.db import models
from django.conf import settings

from eksiapp.managers import TitleManager, EntryManager


class Title(models.Model):
    title_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField("date published", null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)

    objects = TitleManager()

    def __str__(self):
        return self.title_text


class Entry(models.Model):
    title = models.ForeignKey('Title', related_name='entries')
    pub_date_entry = models.DateTimeField("date published", null=True)
    entry_text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)

    objects = EntryManager()

    def __str__(self):
        return self.entry_text
