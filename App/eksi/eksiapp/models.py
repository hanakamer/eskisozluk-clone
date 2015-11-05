from django.db import models
from django.conf import settings

# Create your models here.

class Title(models.Model):
    title_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField("date published", null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    def __str__(self):
        return self.title_text

    def n_entries(self):
        return self.entry_set.count()




class Entry(models.Model):
    title = models.ForeignKey('Title')
    pub_date_entry = models.DateTimeField("date published", null=True)
    entry_text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    def __str__(self):
        return self.entry_text
    def topic_of_enry(self):
        return self.title.values_list("title",flat=True)
