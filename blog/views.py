from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from .models import Post, Comment, Message
from django.contrib.auth.models import User
from django.contrib.auth import login
# Create your views here.

def post_comment(request):
    if request.method == 'POST':
        post_id = request.POST['subject']
        post = Post.objects.get(id = post_id)
        message = request.POST['message']
        print(message)
        
        if not request.user.is_authenticated:     
            name = request.POST['name']
            email = request.POST['email']
            
            try:
                username = User.objects.count() + 1
                user = User.objects.create_user(username = username,  password = 'woury380379efheio')
                user.first_name = name
                user.save()
                login(request, user)
                print(message)
                com = Comment.objects.create(content = message, commenter = user, post = post)
                com.save()
            except:
                return redirect('view-post', post_id)
        else:
            print('okay')
            try:
                
                com = Comment.objects.create(content = message, commenter = request.user, post = post)
                print('try')
            
            except:
                print('except')
                return redirect('view-post', post_id)

    return redirect('view-post', post_id)


def view_post(request, post_id):
    recent_posts = Post.objects.order_by('-published_date')[0:5]
    for p in recent_posts:
        print(p)
    posts = Post.objects.order_by('-published_date')
    post = Post.objects.get(id = post_id)
    comments = Comment.objects.filter(post = post_id)

    return render(request, 'blog/post.html', {'post':post, 'posts': posts, 'comments': comments, 'recent_posts': recent_posts})

def blog(request):
    posts = Post.objects.order_by('-published_date')
    recent_posts = Post.objects.order_by('-published_date')

    #Set up pagination 
    p = Paginator(posts, 10)
    page = request.GET.get('page')
    posts = p.get_page(page)

    return render(request, 'blog/index.html', {'posts': posts, 'recent_posts': recent_posts})
