from django.shortcuts import render,redirect
from main.forms import Productform,Categoryform
from main.models import Product,Category
from django.contrib.auth.decorators import login_required

# Create your views here.

#admin views

def home(request):
    form  = Productform()
    products = Product.objects.all()
    if request.method == "POST":
        form = Productform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list')
    return render(request, 'main/home.html',{'form':form})

def list(request):
    products = Product.objects.all()
    return render(request,'main/list.html',{'products':products})

def update(request,product_id):
    product = Product.objects.get(id=product_id)
    form  = Productform(instance=product)
    if request.method == 'POST':
        form = Productform(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('list')
    return render(request,'main/update.html',{'form':form,'product':product})

def delete(request,product_id):
    if request.method == 'POST':
        Product.objects.get(id=product_id).delete()
        return redirect('list')


def category(request):
    form = Categoryform()
    categorys = Category.objects.all()
    if request.method == 'POST':
        form = Categoryform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category')
    return render(request, 'main/category.html',{'form':form,'categorys':categorys})

def delete_category(request,category_id):   
    if request.method == 'POST':
        Category.objects.get(id=category_id).delete()
        return redirect('category')
    
def update_category(request,category_id):
    category = Category.objects.get(id=category_id)
    form  = Categoryform(instance=category)
    if request.method == 'POST':
        form = Categoryform(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('category')
    return render(request,'main/update_category.html',{'form':form,'category':category})


#user views

#landing views
@login_required
def index(request):
    context = {}
    return render(request,'index.html',context)


