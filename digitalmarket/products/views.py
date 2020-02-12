from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import Http404
from .forms import ProductAddForm


# Create your views here.

def create_view(request):
    form = ProductAddForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        title = data.get("title")
        description = data.get("description")
        price = data.get("price")
        new_obj = Product.objects.create(title=title, description=description, price=price)
    template = 'create_view.html'
    context={
        "form": form,
    }
    return render(request, template, context)


def detail_slug_view(request, slug=None):
    product = get_object_or_404(Product, slug=slug)
    # product=1
    template='detail_view.html'
    context={
        "object": product
    }
    return render(request, template, context)


def detail_view(request, object_id=None):
    product = get_object_or_404(Product, id=object_id)
    template='detail_view.html'
    context={
        "object": product
    }
    return render(request, template, context)


def list_view(request):
    #list of itmes
    print(request)
    template='list_view.html'
    context={}
    return render(request, template, context)
