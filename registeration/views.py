from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

def signup(request):

    if request.method == 'POST':
      username = request.POST['username']
      email = request.POST['email']
      password = request.POST['password']

      if User.objects.filter(username=username).exists():
        messages.info(request,'Username Taken')
        return redirect('signup')

      elif User.objects.filter(email=email).exists():
        messages.info(request, 'Email taken')
        return redirect('signup')

      else:
        user = User.objects.create_user(username=username, password = password, email=email)
        user.save();
        request.session["user"]=username
        auth.login(request, user)
        return redirect('/')

    else:
      return render(request, 'registeration/signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
           auth.login(request, user)
           request.session["user"]=username
           return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('signin')

    return render(request, 'registeration/signin.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
    # return render(request, 'registera tion/signout.html')
