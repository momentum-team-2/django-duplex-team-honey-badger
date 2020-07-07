from django.shortcuts import render, redirect, get_object_or_404
from .models import Snippet
from .forms import SnippetForm
from django.contrib.auth.decorators import login_required

def home(request):
    if request.user.is_authenticated:
        return redirect('list_snippets')

    return render(request, 'snippets/home.html')

@login_required
def list_snippets(request):
    snippets = Snippet.objects.all().order_by('-id')
    return render(request, 'snippets/list_snippets.html', {'snippets': snippets})

@login_required
def show_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    form = SnippetForm()
    return render(request, 'snippets/show_snippet.html', {'snippet': snippet, 'pk': pk, 'form': form})

def add_snippet(request):
    if request.method == 'GET':
        form = SnippetForm()
    else:
        form = SnippetForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_snippets')

    return render(request, 'snippets/add_snippet.html', {'form': form})

def edit_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.method == 'GET':
        form = SnippetForm(instance=snippet)
    else:
        form = SnippetForm(data=request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            return redirect(to='list_snippets')

    return render(request, 'snippets/edit_snippet.html', {'form': form, 'snippet': snippet})

def delete_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.method == 'POST':
        snippet.delete()
        return redirect(to='list_snippets')
    
    return render(request, 'snippets/delete_snippet.html', {'snippet': snippet})