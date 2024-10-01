from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from BApp.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
def Registration(request):
    if request.method == 'POST':
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        
        if User.objects.filter(username=username).exists():
            messages.info(request, "Username Already Taken")
            return redirect('registration')
        else:
            User.objects.create_user(
                first_name=first_name,
                last_name=last_name, 
                username=username,
                email=email,
                password=password,
            )
            messages.info(request, "Successfully Created")
            return redirect('logins')
            
    return render(request, 'Registration.html')

def logins(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if username=='Admin':
            login(request, user)
            return redirect('adashboard')
        elif user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, "Incorrect Password or Username")
            return redirect('logins')
            
    return render(request, 'Logins.html')

@login_required
def dashboard(request):    
    if request.method=='POST':
        datafetch = request.POST
        author = request.user
        postc_id = datafetch.get('postc')
        data = datafetch.get('data')
        postc=Post.objects.get(id=postc_id)
        commentss = comment.objects.create(
            author=author,
            postc = postc,
            data = data
        )
    commentsss = comment.objects.all()
    if request.method =='GET':
        data = request.GET
        postcc = data.get('search','')
        allpost = Post.objects.filter(title__icontains=postcc).order_by('-created_at')
        return render(request, 'Dashboard.html', context={'users': request.user,'allpost':allpost,'commentss':commentsss})

    messages.info(request, "LOGIN SUCCESSFULLY")
    user = request.user
    allpost = Post.objects.all().order_by('-created_at')
    return render(request, 'Dashboard.html', context={'users': user,'allpost':allpost,'commentss':commentsss})



@login_required
def logouts(request):
    logout(request)
    return redirect('logins')

@login_required
def create(request):
    if request.method == 'POST':
        data = request.POST
        title = data.get('title')
        content = data.get('content')
        pic = request.FILES.get('image')

        Post.objects.create(
            title=title,
            content=content,
            pic=pic,
            author=request.user
        )
        messages.info(request,'Blog Posted')
        return redirect('dashboard')
        
    return render(request, 'Create.html')

@login_required
def blogspost(request, author_id):
    author = get_object_or_404(User, id=author_id)
    postss = Post.objects.filter(author=author)
    return render(request, 'Myblogs.html', {'posts': postss})

@login_required
def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    Comment = comment.objects.filter(postc=post)
    return render(request, 'post_detail.html', {'post': post,'Comment':Comment})

@login_required
def post_dlt(request,id):
    post = Post.objects.get(id=id)
    post.delete()
    url = reverse('blogspost', args=[request.user.id]) 
    return redirect(url)

@login_required
def post_upd(request,id):

    post = Post.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        title = data.get('title')
        content = data.get('content')
        pic = request.FILES.get('image')

        post.title=title
        post.content=content
        if pic:
            post.pic=pic
        post.author=request.user
        post.save()
        messages.info(request,'Blog Updated')
        
        url = reverse('blogspost', args=[request.user.id]) 
        return redirect(url)
    return render(request,'update.html', context={'post':post})

@login_required
def comment_dlt(request,id):
    comments = comment.objects.get(id=id)
    comments.delete()
    return redirect('/dashboard/')

@login_required
def admin_dashboard(request):
    posts=Post.objects.all().count()
    users=User.objects.all().count()
    return render (request,'Adashboard.html', context={'posts':posts,'users':users})

@login_required
def blogs(request):
    Posts=Post.objects.all()
    return render (request,'Allblogs.html', context={'Posts':Posts})

@login_required
def post_adlt(request,id):
    post = Post.objects.get(id=id)
    post.delete() 
    return redirect('/adashboard/')


@login_required
def post_aupd(request,id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        title = data.get('title')
        content = data.get('content')
        pic = request.FILES.get('image')

        post.title=title
        post.content=content
        if pic:
            post.pic=pic
        post.author=request.user
        post.save()
        return redirect('/adashboard/')
    return render(request,'Aedits.html', context={'post':post})

@login_required
def adashboard(request):    
    commentsss = comment.objects.all()
    allpost = Post.objects.all().order_by('-created_at')
    users = User.objects.all().count()
    return render(request, 'Allblogs.html', context={'allpost':allpost,'commentss':commentsss ,'users':users})

@login_required
def comment_adlt(request,id):
    comments = comment.objects.get(id=id)
    comments.delete()
    return redirect('/adashboard')

@login_required
def users(request):
    usersn = User.objects.annotate(post_count = Count('post'))
    return render(request , 'Ausers.html', context={'usersn':usersn})

@login_required
def posts(request):
    posts = Post.objects.all()
    return render(request , 'Apost.html', context={'posts':posts})

@login_required
def user_adlt(request,id):
    users = User.objects.get(id=id)
    users.delete()
    return redirect('/users')

@login_required
def post_adlt(request,id):
    posts = Post.objects.get(id=id)
    posts.delete()
    return redirect('/posts')


# def user_edits(request,id):

#     user = User.objects.get(id=id)
#     if request.method == 'POST':
#         data = request.POST
#         first_name = data.get('first_name')
#         last_name = data.get('last_name')
#         username = data.get('username')

#         user.first_name = first_name
#         user.last_name=last_name
#         user.username =username
#         user.save()
#         return redirect()
#     return render(request,'Eusers.html', context={'user':user})
