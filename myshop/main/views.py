from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm
from .models import Product
from django.views.decorators.http import require_POST

def home(request):


    return render(request, 'main/home.html')

def shop(request):
    products = Product.objects.all()

    data = {'products': products}

    return render(request, 'main/shop.html', data)
def contacts(request):
    return render(request, 'main/contacts.html')
def about(request):
    return render(request, 'main/about.html')

def addproduct(request):

    form = ProductForm()

    error = ''
    # if request.method == 'POST':
    #     form = ProductForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('shop')
    #     else:
    #         error = form.errors
    #
    #
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print('NO ERROR')
            return redirect('shop')  # Замените 'product_list' на ваш URL для списка продуктов
    else:
        error = form.errors
        print('ERROR')
    data = {'form': form,
             'error': error}
    return render(request, 'main/addproduct.html', data)



    return render(request, 'main/addproduct.html',data)



