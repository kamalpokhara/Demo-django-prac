from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
# Create your views here.
from home.models import Article
from .serailizers import ArticleSerializer


def index(request):
    articles =  Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    message = {

        'message': "Welcome to the Article API!",
        'status': "success",
        'code': 200,
        'articles': serializer.data
    }
    
    return JsonResponse(message)

from django.views.decorators.csrf import csrf_exempt
@require_POST
@csrf_exempt
def create(request):
    if request.method == "POST":
        data = request.POST
        article = Article.objects.create(
            title=data.get("title"),
            content=data.get("content")
        )
        serializer = ArticleSerializer(article)
        message = {
            'message': "Article created successfully!",
            'status': "success",
            'code': 201,
            'article': serializer.data
        }
        return JsonResponse(message, status=201)

def detail(request, slug):
    object = Article.objects.get(slug=slug)
    serializer = ArticleSerializer(object)

    return JsonResponse(serializer.data, safe=False)   

def delete(request, slug):
    return JsonResponse({"message": f"Delete article with slug: {slug}"})
