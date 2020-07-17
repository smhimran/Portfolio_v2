from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from .forms import PostForm
from django.utils import timezone
from cloudinary import uploader, api

# Create your views here.
def home(request):
    post_list = Post.objects.order_by('-timestamp')
    page = request.GET.get('page', 1)
    if page:
        paginator = Paginator(post_list, 4)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/index.html', {'posts': posts})

def detail(request, slug):
    post = Post.objects.get(slug=slug)
    try:
        prev = post.get_previous_by_timestamp()
    except ObjectDoesNotExist:
        prev = None

    try:
        nxt = post.get_next_by_timestamp()
    except ObjectDoesNotExist:
        nxt = None


    return render(request, 'blog/blog-post.html', {'post': post, 'prev': prev, 'nxt': nxt})

def all(request):
    post_list = Post.objects.all()
    page = request.GET.get('page', 1)
    if page:
        paginator = Paginator(post_list, 4)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/blog-list.html', {'posts': posts})

def write(request):
    if request.method == "GET":
        form = PostForm()
        return render(request, 'blog/write-blog.html', {'form': form})
    else:
        form = PostForm(request.POST)
        title = request.POST['title']
        timestamp = timezone.now()
        if form.is_valid():
            post = form.save(commit=False)
            post.title = title
            post.timestamp = timestamp
            banner = request.FILES.get('banner')
            print(banner)
            print('----------------------------------------------------------------------------------')
            if banner:
                # banner = request.FILES['banner']
                info = uploader.upload(banner)
                post.banner = info['url']

            post.save()

            suc_msg = 'Success!'
            return render(request, 'blog/write-blog.html', {'suc_msg': suc_msg})

        else:
            err_msg = 'Error! invalid format.'
            return render(request, 'blog/write-blog.html', {'err_msg': err_msg})

def edit(request, slug):
    if request.method == "GET":
        post = Post.objects.get(slug=slug)
        form = PostForm(instance=post)
        return render(request, 'blog/edit-blog.html', {'form': form, 'post': post})
    else:
        post = Post.objects.get(slug=slug)
        form = PostForm(request.POST, instance=post)
        title = request.POST['title']
        timestamp = timezone.now()
        if form.is_valid():
            post = form.save(commit=False)
            post.title = title
            post.timestamp = timestamp
            banner = request.FILES.get('banner')
            print(banner)
            print('----------------------------------------------------------------------------------')
            if banner:
                # banner = request.FILES['banner']
                info = uploader.upload(banner)
                post.banner = info['url']

            post.save()

            suc_msg = 'Success!'
            return render(request, 'blog/edit-blog.html', {'suc_msg': suc_msg})

        else:
            err_msg = 'Error! invalid format.'
            return render(request, 'blog/edit-blog.html', {'err_msg': err_msg})