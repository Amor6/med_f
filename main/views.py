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
    serv_cat = Services.objects.get(category_id=pk)
    context = {
        'object_l': serv_cat.name_serv,
        'pay': serv_cat.price,
        'serv_description': serv_cat.serv_description,
        'title_l': f'Направление: {category_item.name}',
        'description': f'Описание направления: {category_item.description}',

    }
    return render(request, 'main/includes/serv.html', context)
