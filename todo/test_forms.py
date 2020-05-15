from django.test import TestCase
from .forms import ItemForm

# Create your tests here.
class TestToDoItemForm(TestCase):
    """Methods MUST begin with 'test_'."""
    def test_can_create_an_item_with_just_a_name(self):
        form = ItemForm({'name': 'Create Tests'})
        self.assertTrue(form.is_valid())

    """Asserts that, when the 'name' attribute isn't provided, that the form 
    is NOT valid. Also asserts that the 'name' field not being provided gives 
    the error message 'This field is required.'."""
    def test_correct_message_for_missing_name(self):
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u'This field is required.'])
