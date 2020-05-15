from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Item

# Create your tests here.
class TestViews(TestCase):
    def test_get_home_page(self):
        """We use '.client' to send a fake request to the url, asking 
        for the "/" URL route. We then assert that the page's status 
        code is equal to '200', meaning that the request has worked."""
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)

        """Here we assert that the page's template used is the 
        'todo_list.html' template."""
        self.assertTemplateUsed(page, "todo_list.html")

    def test_get_add_item_page(self):
        page = self.client.get("/add")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item_form.html")

    def test_get_edit_item_page(self):
        """First we have to create an item with a name, for the 
        purposes of having something to edit"""
        item = Item(name='Create A Test')
        item.save()

        """We pass through the URL, where {0} is equal to the item's 
        id."""
        page = self.client.get("/edit/{0}".format(item.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item_form.html")
    
    def test_get_edit_page_for_item_that_does_not_exist(self):
        """Here we run a request for a nonexistent URL, and then verify 
        that we get a status code of '404', meaning that the page was 
        not found."""
        page = self.client.get("/edit/1")
        self.assertEqual(page.status_code, 404)

    def test_post_create_an_item(self):
        """Creates an item with the 'name' of "Create A Test"."""
        response = self.client.post("/add", {'name': "Create A Test"})
        item = get_object_or_404(Item, pk=1)
        """Asserts that the 'done' status of the item is False."""
        self.assertFalse(item.done)

    def test_post_edit_an_item(self):
        item = Item(name='Create A Test')
        item.save()
        """We create a variable called 'id', which stores the item's 
        id."""
        id = item.id
        response = self.client.post("/edit/{0}".format(id), {'name': "A Different Name"})

        item = get_object_or_404(Item, pk=id)

        self.assertEqual(item.name, 'A Different Name')

    def test_toggle_status(self):
        item = Item(name='Create A Test')
        item.save()
        """We create a variable called 'id', which stores the item's 
        id."""
        id = item.id
        response = self.client.post("/toggle/{0}".format(id))

        item = get_object_or_404(Item, pk=id)
        self.assertTrue(item.done)
