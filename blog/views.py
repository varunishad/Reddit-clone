from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Comments, Post
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from . import forms
from django.contrib.auth.models import User
from registeration.views import signin
from django.urls import resolve
from .forms import PostComment, PostForm

@login_required
def comment(request, pk):
    if request.session.has_key('user'):
        username = request.session['user']

    user_obj = Post.objects.get(id=pk)

    form = PostComment()
    if request.method == "POST":
        form = PostComment(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.user_post = user_obj
            instance.save()
            return redirect("./"+ str(pk))

    comments_order = Comments.objects.filter(user_post=user_obj).order_by('-created_on')

    context = {
        'form' : form,
        'post' : user_obj,
        'comments' : comments_order,
        'username': username
    }

    return render(request, 'openpost.html', context)


def search(request):
    if request.method == "POST":
        try:
            searched = request.POST['searched']
            posts = Post.objects.filter(title__icontains=searched)
            users=User.objects.filter(username__icontains=searched)
            return render(request,'search_results.html', {'searched': searched,'posts':posts,"users":users })
        except:
            return render(request,'search_results.html')
    else:
        return render(request,'search_results.html')


def create(request):
    form = forms.PostForm()
    if request.method == 'POST':
        form = forms.PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            curr_user = User.objects.get(username=request.session["user"])
            post.uploader = curr_user
            post.save()
            return redirect('/blog/myprofile/{}'.format(curr_user))

    return render(request, 'createpost.html', {'form':form})

def delete(request, pk):
    if request.session.has_key('user'):
        username = request.session['user']
        post = Post.objects.get(pk=pk)
        post_username = post.uploader.username
        # user_object = User.objects.get(username=username)
        # curr_user_id = User.objects.filter(username = username).values_list('id')[0][0]
        if username == post_username:
            Post.objects.filter(id=post.id).delete()

        if request.method == 'POST':
            next = request.POST.get('next_url')
            return redirect(next)
        else:
            return redirect('/')
    else:
        return redirect('/')

# @login_required

# @login_required
def likes(request, pk):
    if request.session.has_key('user'):
        username = request.session['user']
        post = Post.objects.get(pk=pk)
        user_object = User.objects.get(username=username)
        if user_object not in post.likes.all():
            post.likes.add(user_object)
        else:
            post.likes.remove(user_object)

        count_likes = post.likes.all().count()
        return count_likes
    else:
        # print('------------------------------------')
        return  redirect('/registeration/signin/')
        # return HttpResponseRedirect('/registeration/signin/')
        # return redirect('/registeration/signin')


def dislikes(request, pk):
    if request.session.has_key('user'):
        username = request.session['user']
        post = Post.objects.get(pk=pk)
        user_object = User.objects.get(username=username)
        if user_object in post.likes.all():
            post.likes.remove(user_object)
        else:
            post.likes.add(user_object)

        count_likes = post.likes.all().count()
        return count_likes

    else:
        return render(request, 'registeration/signin.html')

def home(request):
    count_likes = 0
    like = False
    if request.method == "POST":
        value = request.POST.get('post_id')
        # pk = value[:len(value)-1]
        # vote = value[-1]
        # if vote == 'u':
        #     count_likes= likes(request, pk)
        # elif vote == 'd':
        #     count_likes = dislikes(request, pk)
        count_likes=likes(request,value)

    posts = Post.objects.all().order_by('-date_created')

    try:
        request.session["user"]
    except:
        user = None
    context = {
        'posts': posts,
        'count_likes': count_likes,
        'like': like,
    }

    if request.session.has_key('user'):
        username = request.session['user']
        user_obj = User.objects.get(username=username)
        return render(request, 'home.html', context)

    return render(request, 'home.html', context)


def myprofile(request,username):
    count_likes = 0
    if request.method == "POST":
        value = request.POST.get('post_id')
        # pk = value[:len(value)-1]
        # vote = value[-1]
        # if vote == 'u':
        #     count_likes= likes(request, pk)
        # elif vote == 'd':
            # count_likes = dislikes(request, pk)
        count_likes=likes(request,value)

    curr_user_id = User.objects.filter(username = username).values_list('id')
    posts = Post.objects.filter(uploader=curr_user_id[0]).order_by('-date_created')
    context = {
        'posts': posts,
        'username': username,
        'count_likes': count_likes
    }

    return render(request, 'myprofile.html', context)

