from django.shortcuts import render, get_object_or_404,redirect
from cart.forms import CartAddProductForm
from .models import Category, Product,ContactUs
from .forms import ContactForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
# from django.views import generic

# class IndexView(generic.ListView):
#     template_name = 'shop/index.html'
#     context_object_name = 'products'

#     def get_queryset(self):
#         '''Return five lattest products
#         '''
#         return Product.objects.filter(created__lte=timezone.now()
#         ).order_by('-created')[:5]


@login_required
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {'category': category, 'categories': categories, 'products': products}
    return render(request, 'shop/product/list.html', context)


# class ProductListView(generic.ListView):
#     template_name = 'shop/product/list.html'

#     def get_queryset(self):
#         return Product.objects.filter(available=True)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         category = None
#         if category_slug:
#             category = get_object_or_404(Category, slug=category_slug)
#         context['category'] = category
#         context['categories'] = Category.objects.all()





def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {'product': product, 'cart_product_form': cart_product_form}
    return render(request, 'shop/product/detail.html', context)


# class ProductDetialView(generic.DetailView):

#     template_name = 'shop/product/detail.html'
#     model = Product
#     form_class = CartAddProductForm

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['products'] = get_object_or_404(Product, 
#         id=id, slug=slug, available=True)
#         return context
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'shop/base/sucess.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'shop/base/contact.html', context)

def about(request):
    return render(request, "shop/base/about.html")

def