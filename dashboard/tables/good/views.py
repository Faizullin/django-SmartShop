from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, get_object_or_404

from SmartShop.models import *
from .forms import *


@login_required()
def good_index(request):
    goods = Good.objects.all()
    context = {
        'segment': 'good_index',
        'goods': goods,
        'form': GoodForm()
    }
    html_template = loader.get_template('dashboard/tables/good/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required()
def good_create(request):
    if request.method == 'POST':
        form = GoodForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = GoodForm()
    return render(request, 'good_form.html', {'form': form})

@login_required()
def good_edit(request, pk):
    good = get_object_or_404(Good, pk=pk)
    if request.method == 'POST':
        form = GoodForm(request.POST, instance=good)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = GoodForm(instance=good)
    return render(request, 'good_form.html', {'form': form})