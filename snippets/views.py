from django.shortcuts import render, redirect, get_object_or_404
from .models import Snippet
from .forms import SnippetForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView
from django.db.models import Q
# from django_gravatar.helpers import get_gravatar_url, has_gravatar, get_gravatar_profile_url, calculate_gravatar_hash



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
            snippet = form.instance
            snippet.user = request.user
            snippet.save()
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

def copy_snippet (request, pk):
    original_snippet = get_object_or_404(Snippet, pk=pk)
    copied_snippet = Snippet()
    copied_snippet.title = original_snippet.title
    copied_snippet.language = original_snippet.language
    copied_snippet.code = original_snippet.code
    copied_snippet.description = original_snippet.description
    copied_snippet.user = request.user
    copied_snippet.original_snippet = original_snippet
    copied_snippet.save()
    return redirect(to='list_snippets')


def profile (request):
    # url = get_gravatar_url(request.user.email, size=150)
    # gravatar_exists = has_gravatar('bob@example.com')
    # profile_url = get_gravatar_profile_url('alice@example.com')
    # email_hash = calculate_gravatar_hash('alice@example.com')
    return render(request, 'snippets/profile.html')


def search(request):
    query = request.GET.get('search_string')
    snippets = Snippet.objects.filter(Q(title__icontains=query))
    return render(request, "snippets/list_snippets.html", {"snippets" : snippets})