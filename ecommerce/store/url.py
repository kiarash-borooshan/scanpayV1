from django.urls import path

from . import views


app_name = "store"

urlpattens = [
    path("", views.store, name=""),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
]