from django.test import TestCase
from eksiapp.entry_creation import create_entry_with_title
# Create your tests here.
from .models import Title, Entry

# class TestEntryCreation(TestCase):
#
#     def test_entry_creation(self):
#         create_entry_with_title('Deneme', 'Denemenin tanimi')
#         create_entry_with_title('Deneme', 'Denemenin tanimi')
#
#         assert Title.objects.filter(title_text='Deneme').exists()
#         assert Entry.objects.filter(title__title_text='Deneme').count() == 2
