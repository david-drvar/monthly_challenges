from django.http import HttpResponse
from django.shortcuts import render

posts = [

]


def index(request):
    return render(request, "blog/index.html")


def all_posts(request):
    return render(request, "blog/all-posts.html")


def post_detail(request, slug):
    return render(request, "blog/post-detail.html")