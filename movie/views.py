from django.shortcuts import render, get_object_or_404
from .models import Post
from .utils import get_page,prev_next_post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def index(request):
    post_list = Post.objects.all().order_by('-pub_date')
    page = get_page(request)
    paginator = Paginator(post_list, 10) 
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {'posts' : posts}
    return render(request, 'movie/index.html', context)
def post(request, id):
    post = get_object_or_404(Post, pk=id)
    prev_post,next_post = prev_next_post(id)
    return render(request, 'movie/post.html', {'post':post, 'prev_post': prev_post, 'next_post':next_post})
