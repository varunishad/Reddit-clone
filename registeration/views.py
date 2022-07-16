from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

def signup(request):

    if request.method == 'POST':
      username = request.POST['username']
      email = request.POST['email']
      password = request.POST['password']

      if len(username.rstrip()) < 1:
        messages.info(request,'Invalid Username')
        return redirect('/registeration/signup')

      elif User.objects.filter(username=username).exists():
        messages.info(request,'Username Taken')
        return redirect('/registeration/signup')

      elif len(email.rstrip()) < 1:
        messages.info(request, 'invalid email')
        return redirect('/registeration/signup')

      elif len(password.rstrip()) < 1:
        messages.info(request, 'Invalid Password')
        return redirect('/registeration/signup')

      elif User.objects.filter(email=email).exists():
        messages.info(request, 'Email taken')
        return redirect('/registeration/signup')

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

        if len(username.rstrip()) < 1:
          messages.info(request,'Invalid Username')
          return redirect('/registeration/signin')

        elif len(password.rstrip()) < 1:
          messages.info(request, 'Invalid Password')
          return redirect('/registeration/signin')

        else:
            auth.login(request, user)
            request.session["user"]=username
            return redirect('/blog/home')

    return render(request, 'registeration/signin.html')

def logout(request):
    if request.session.has_key('user'):
      del request.session['user']
    auth.logout(request)
    return redirect('/')
