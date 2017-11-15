from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
    posts = Post.objects.order_by('created_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
