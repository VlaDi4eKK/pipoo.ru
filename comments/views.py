# coding=utf-8
from django.http import Http404
from django.shortcuts import render_to_response
from catalog.models import Category, Video
from comments.models import Comment

# Create your views here.
def comment(request, url_categ, url_video):
    try:
        categ = Category.objects.get(url=url_categ)
        video = Video.objects.get(url=url_video)

    except:
        raise Http404
    return render_to_response("comment.html", {'categ': categ, 'video': video, 'comments': Comment.objects.filter(video_id=video.id)})
