from django.urls import path
from products.views import product, cartdetails, men
urlpatterns = [
   path('p', product),
   path('cart', cartdetails),
   path('men', men)
]