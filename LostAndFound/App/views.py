from .models import Item
from .models import Category
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect

def item_list(request):
    items = Item.objects.all()
    return render(request, 'items/item_list.html', {'items': items})

@login_required
def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'items/item_detail.html', {'item': item})

@login_required
def item_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        category = Category.objects.get(id=request.POST['category'])
        location = request.POST['location']
        status = request.POST['status']
        image = request.FILES.get('image')
        item = Item.objects.create(
            title=title, description=description, category=category,
            location=location, status=status, image=image, reported_by=request.user
        )
        return redirect('item_list')
    categories = Category.objects.all()
    return render(request, 'items/item_form.html', {'categories': categories})

@login_required
def item_update(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        item.title = request.POST['title']
        item.description = request.POST['description']
        item.category = Category.objects.get(id=request.POST['category'])
        item.location = request.POST['location']
        item.status = request.POST['status']
        if 'image' in request.FILES:
            item.image = request.FILES['image']
        item.save()
        return redirect('item_list')
    categories = Category.objects.all()
    return render(request, 'items/item_form.html', {'item': item, 'categories': categories})

@login_required
def item_delete(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('item_list')