from django.shortcuts import render
from .models import Post
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'posts.html', {'posts':posts})

def new(request):
    if request.method == 'POST' :
        title = request.POST['title']
        body = request.POST['body']
        if(Post.objects.filter(title=title).exists()):
            messages.info(request, 'Blog\'s Title Exists Already')
            return redirect('/new')
        else:      
            obj = Post.objects.create(title=title, body=body)
            obj.save()
            return redirect('/')
    return render(request, 'newpost.html')

