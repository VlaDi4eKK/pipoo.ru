from django.http import Http404
from django.shortcuts import render_to_response
from catalog.models import Category, Video


def home(request):
    try:
        categories = Category.objects.filter(parent=None)
        for parent in categories:
            parent.categories = Category.objects.filter(parent=parent)
    except Category.DoesNotExist:
        raise Http404
    return render_to_response("index.html", {'categories': categories})


def category_view(request, url):
    try:
        categ = Category.objects.get(url=url)
        videos = Video.objects.filter(category=categ)
    except Category.DoesNotExist:
        raise Http404
    return render_to_response("category.html", {'categ': categ, 'videos': videos})


def video_view(request, url_categ, url_video):
    try:
        categ = Category.objects.get(url=url_categ)
        video = Video.objects.get(url=url_video)
    except:
        raise Http404
    return render_to_response("video.html", {'categ': categ, 'video': video})
