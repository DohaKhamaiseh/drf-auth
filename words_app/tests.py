from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Word


# Create your tests here.

class ThingTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_thing = Word.objects.create(name='flower', talker=testuser1, desc="test desc ...")
        test_thing.save()

    def thigs_model(self):
        word = Word.objects.get(id=1)
        actual_talker= str(word.talker)
        actual_word = str(word.word)
        actual_desc = str(word.desc)
        self.assertEqual(actual_talker,"testuser1")
        self.assertEqual(actual_word,"flower")
        self.assertEqual(actual_desc,"test desc ...")
