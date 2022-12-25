from django.test import TestCase

from classtab_main.models import Dummy


class TestClasstabMain(TestCase):
    # (例) dummyのnameフィールドの等価性テスト
    def test_dummy_name_equality(self):
        dummy = Dummy(name="I am dummy!")
        self.assertEqual(dummy.name, "I am dummy!")
