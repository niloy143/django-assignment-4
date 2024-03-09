from django.shortcuts import render
from .forms import CategoryForm
from .models import Category

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()

    form = CategoryForm()
    categories = Category.objects.all()
    return render(request, 'add_category.html', {'form': form, 'categories': categories})