from django.shortcuts import get_object_or_404,redirect, render
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context= {
        'articles':articles
    }
    return render(request, 'index.html', context)

def create(request):
    if request.method =='POST':
        title =request.POST.get('title')
        content = request.POST.get("content")
        article = Article.objects.create(title=title, content = content)
        return redirect('articles.home')
    return render(request, 'create.html')

def detail(request,slug):
    context = {
        'article':Article.objects.get(slug=slug)

    }
    return render(request, 'detail.html', context)


def delete(request,slug):
    article = get_object_or_404(Article, slug=slug)

    if request.method =='POST':
        article.delete()
        return redirect('articles:home')

    # for get
    return render(request, "delete.html", {"article": article})


def update(request, slug):
    article = Article.objects.get(slug=slug)
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        article.title = title
        article.content = content
        article.save()
        return redirect("articles:detail", slug=slug)
    context = {"article": article}
    return render(request, "update.html", context)
