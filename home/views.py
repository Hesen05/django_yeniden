from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def about_us(request):
    return render(request,'about_us.html')

def blog(request):
    return render(request, 'blog.html')

def productdetail(request):
    return render(request,'product-detail.html')

def productlist(request):
    return render(request,'product-list.html')

def quickview(request):
    return render(request,'quick_view.html')

def shopping_cart(request):
    return render(request,'shopping_carrt.html')

def faq(request):
    return render(request, 'faq.html')

def contactus(request):
    return render(request, 'contact_us.html')

def contactinformation(request):
    return render(request, 'contact_information.html')

def checkout(request):
    return render(request, 'checkout.html')

def checkoutbillinginfo(request):
    return render(request, 'checkout_billing_info.html')

def blogdetail(request):
    return render(request,'blog_detail.html')

def addressbook(request):
    return render(request, 'address_book.html')

def error404(request):
    return render(request, '404error.html')