from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404

from dashboard.decorators import group_required
from SmartShop.models import *
from .forms import *


@login_required()
@group_required(['groupOwner'])
def shop_index(request):
    shops = Shop.objects.all()
    context = {
        'segment': 'shop_index',
        'shops': shops,
        'form': ShopForm()
    }
    html_template = loader.get_template('dashboard/tables/shop/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required()
@group_required(['groupOwner'])
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

@login_required()
@group_required(['groupOwner'])
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