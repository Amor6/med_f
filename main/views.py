from django.shortcuts import render

from main.models import Category, Services


def index(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Наши услуги'
    }
    return render(request, 'main/index.html', context)


def contacts(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Наши контакты'
    }
    return render(request, 'main/contacts.html', context)


def category_main(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_l': Services.objects.filter(category_id=pk),
        'title': f'Услуги {category_item.name}'
    }
    return render(request, 'main/includes/serv.html', context)
