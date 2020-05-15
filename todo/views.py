from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

# Create your views here.


def get_todo_list(request):
    results = Item.objects.all()
    return render(request, "todo_list.html", {'items': results})


def create_an_item(request):
    if request.method == 'POST':
        """request.FILES is used, just incase any files are being transferred"""
        form = ItemForm(request.POST, request.FILES)
        """The form's validity is checked."""
        if form.is_valid():
            form.save()
        return redirect(get_todo_list)
    else:
        """If 'POST' is not the method used, the function returns an empty form"""
        form = ItemForm()
    """In the html, """
    return render(request, "item_form.html", {'form': form})


def edit_an_item(request, id):
    """pk means 'primary key'"""
    item = get_object_or_404(Item, pk=id)

    """If the method used is 'POST' i.e: if we are editing a form, then the form 
    will be saved and we will be redirected back to the 'todo_list.html' page. If 
    the method is 'GET', then the 'item_form.html' page will be loaded, already 
    propagated with the Item's fields."""
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(get_todo_list)
    else:
        """The form is set to what it originally was."""
        form = ItemForm(instance=item)
    return render(request, "item_form.html", {'form': form})


def toggle_status(request, id):
    """pk means 'primary key'"""
    item = get_object_or_404(Item, pk=id)
    item.done = not item.done
    item.save()
    return redirect(get_todo_list)