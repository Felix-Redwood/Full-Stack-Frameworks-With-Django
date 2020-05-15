from django.test import TestCase
from .models import Item

# Create your tests here.
class TestItemModel(TestCase):
    """Here we are trying to verify that if we create an item 
    without specifying the 'done' property, that the item sets 
    to 'false' automatically."""
    def test_done_defaults_to_false(self):
        item = Item(name='Create A Test')
        item.save()

        """Here we make sure that the item's 'name' is 'Create 
        A Test', and that 'done' is set to False."""
        self.assertEqual(item.name, 'Create A Test')
        self.assertFalse(item.done)

    def test_can_create_an_item_with_a_name_and_status(self):
        item = Item(name='Create A Test', done=True)
        item.save()

        """Here we make sure that the item's 'name' is 'Create 
        A Test', and that 'done' is set to True."""
        self.assertEqual(item.name, 'Create A Test')
        self.assertTrue(item.done)

    def test_item_as_a_string(self):
        item = Item(name='Create A Test')
        self.assertEqual('Create A Test', str(item))