from django.test import TestCase

class SmokeTest(TestCase):

    def test_bad_paths(self):
        self.assertEqual(1 + 1, 3)
