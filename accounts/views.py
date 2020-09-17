from django.shortcuts import render,redirect,reverse
from accounts.forms import SignUpForm


def register(request):
    form = SignUpForm()
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            print("saved")
            return redirect(reverse('register'))
    return render(request,'registration/register.html',{'form':form})