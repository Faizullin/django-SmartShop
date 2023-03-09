from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404

from SmartShop.models import *
from .forms import *


@login_required()
def purchase_history_index(request):
    purchase_historys = Purchase.objects.filter(is_completed=True)
    context = {
        'segment': 'purchase_history_index',
        'purchase_historys': purchase_historys,
        'form': PurchaseForm()
    }
    html_template = loader.get_template('dashboard/tables/purchase_history/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required()
def purchase_history_create(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = PurchaseForm()
    return render(request, 'purchase_history_form.html', {'form': form})

@login_required()
def purchase_history_edit(request, pk):
    purchase_history = get_object_or_404(Purchase, pk=pk)
    if request.method == 'POST':
        form = PurchaseForm(request.POST, instance=purchase_history)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = PurchaseForm(instance=purchase_history)
    return render(request, 'purchase_history_form.html', {'form': form})