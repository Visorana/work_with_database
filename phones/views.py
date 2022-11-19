import ast

from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    phone_objects = Phone.objects.all()
    sort = request.GET.get("sort")
    if sort in ('name', 'min_price', 'max_price'):
        if sort in 'name':
            phone_objects = sorted(phone_objects, key=lambda x: x.name)
        elif sort in 'min_price':
            phone_objects = sorted(phone_objects, key=lambda x: x.price)
        elif sort in 'max_price':
            phone_objects = sorted(phone_objects, key=lambda x: x.price, reverse=True)
    phones = {p.name: [p.slug, p.price, p.image] for p in phone_objects}
    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    phone = [phone.name, phone.price, phone.image]
    context = {
        'phone': phone
    }
    return render(request, template, context)
