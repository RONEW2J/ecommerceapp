from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category


# Create your views here.
# List all products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

# View details of a single product
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})

# Create a new product
def product_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category_id = request.POST.get('category')
        price = request.POST.get('price')
        description = request.POST.get('description')

        category = get_object_or_404(Category, id=category_id)
        Product.objects.create(
            name=name,
            category=category,
            price=price,
            description=description
        )
        return redirect('product_list')
    else:
        categories = Category.objects.all()
        return render(request, 'store/product_create.html', {'categories': categories})

# Update an existing product
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.category_id = request.POST.get('category')
        product.price = request.POST.get('price')
        product.description = request.POST.get('description')
        product.save()
        return redirect('product_list')
    else:
        categories = Category.objects.all()
        return render(request, 'store/product_update.html', {'product': product, 'categories': categories})

# Delete a product
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'store/product_confirm_delete.html', {'product': product})