from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone

def home(request):
    return render(request, 'products/home.html')

@login_required
def create(request):
    if request == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['body'] and request.FILES['icon'] and request.FILES['image']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            if request.POST['url'].startwith('http://') or request.POST['url'].startwith('https://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://' + request.POST['url']
            product.body = request.FILES['icon']
            product.body = request.FILES['image']
            product.pub_date = timezone.date.now()
            product.hunter = request.user
            product.save()
            return redirect('home')
        else:
            return render(request, 'products/create.html',{'error':'All fileds must be filled'})
    else:
        return render(request, 'products/create.html')
