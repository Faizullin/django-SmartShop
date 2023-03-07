# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, get_object_or_404

from SmartShop.models import *
from .forms import *

LOGIN_URL = "/auth/login"

@login_required(login_url=LOGIN_URL)
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('dashboard/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url=LOGIN_URL)
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('dashboard/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('dashboard/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('dashboard/page-500.html')
        return HttpResponse(html_template.render(context, request))

@login_required(login_url=LOGIN_URL)
def shop_index(request):
    shops = Shop.objects.all()
    context = {
        'segment': 'shop_index',
        'shops': shops,
        'form': ShopForm()
    }
    html_template = loader.get_template('dashboard/shop/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url=LOGIN_URL)
def shop_create(request):
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ShopForm()
    return render(request, 'shop_form.html', {'form': form})

@login_required(login_url=LOGIN_URL)
def shop_edit(request, pk):
    shop = get_object_or_404(Shop, pk=pk)
    if request.method == 'POST':
        form = ShopForm(request.POST, instance=shop)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ShopForm(instance=shop)
    return render(request, 'shop_form.html', {'form': form})