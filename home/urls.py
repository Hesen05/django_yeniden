from django.urls import path 
from home.views import *

urlpatterns = [
    path('', index),
    path('about/', about_us),
    path('blog/', blog),
    path('blogdetail/', blogdetail),
    path('404error/', error404),
    path('contact/', contactus),
    path('faq/', faq),
    path('product-list/', productlist),
    path('product-detail/', productdetail),
    path('quick-view/', quickview),
    path('shopping_cart/', shopping_cart),
    

]