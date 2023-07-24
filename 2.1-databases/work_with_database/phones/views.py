from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    if sort:
        if sort == 'name':
            object_sorted = Phone.objects.all().order_by('name')
        elif sort == 'min_price':
            object_sorted = Phone.objects.all().order_by('price')
        elif sort == 'max_price':
            object_sorted = Phone.objects.all().order_by('-price')
    else:
        object_sorted = Phone.objects.all()

    context = {
        'phones': object_sorted
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        'phone': Phone.objects.get(slug=slug)
    }
    return render(request, template, context)
