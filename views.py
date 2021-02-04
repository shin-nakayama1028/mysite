from django.http import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .models import Memo
from .forms import MemoForm

def show(request):
    
    memos = Memo.objects.order_by('content')
    return TemplateResponse(request, 'show.html', {'memos': memos})

def create(request):
    if request.method == 'GET': 
        form = MemoForm()
        return render (request, 'create.html', {'form': form})
    
    elif request.method == 'POST':
        form = MemoForm(request.POST)
        if form.is_valid():
            memo = form.save(commit=False)
            memo.save()
            return TemplateResponse(request, 'detail.html',
                            {'memo': memo,
                             'back_view': 'create'})
            
def detail(request, id):
    try:
        memo = Memo.objects.get(id=id)
    except Memo.DoesNotExist:
        raise Http404
    return TemplateResponse(request, 'detail.html',
                            {'memo': memo,
                             'back_view': 'detail'})


def delete(request, id):
    try:
        memo = Memo.objects.get(id=id)
    except Memo.DoesNotExist:
        raise Http404
    if request.method == 'POST':
        memo.delete()

    memos = Memo.objects.order_by('content')
    return TemplateResponse(request, 'show.html', {'memos': memos})
    
    