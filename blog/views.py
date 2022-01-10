from django.shortcuts import render, redirect
from .models import Post
# from .forms import PostForm
from . import forms
from django.contrib.auth.models import User

def create(request):
    form = forms.PostForm()
    # print('user:-------',request.session['user'])
    if request.method == 'POST':
        form = forms.PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            curr_user = User.objects.get(username=request.session["user"])
            print(curr_user)

            post.uploader = curr_user
            post.save()
            return redirect('/myprofile')

    return render(request, 'createpost.html', {'form':form})

# @login_required
def myprofile(request):
    username = request.session["user"]
    curr_user_id = User.objects.filter(username = username).values_list('id')
    posts = Post.objects.filter(uploader=curr_user_id[0]).order_by('-date_created')
    context = {
        'posts': posts,
        'username': username
    }
    return render(request, 'myprofile.html', context)

# @login_required
def home(request):
    posts = Post.objects.all().order_by('-date_created')
    context = {
        'posts': posts,
    }
    return render(request, 'home.html', context)
