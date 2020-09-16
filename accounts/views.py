from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from accounts.forms import SignUpForm
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get(password)
            user = authenticate(username=username,password=raw_password)
            login(request,user)
            return redirect('home')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request,'signup.html',context)

def login(request):
    context = {}
    return render(request,'login.html',context)