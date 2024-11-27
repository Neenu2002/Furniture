from django.urls import path
from WebApp import views

urlpatterns = [
    path('home/',views.homepage,name="home"),
    path('products_page/',views.productspage,name="products_page"),
    path('contacts/',views.contactspage,name="contacts"),
    path('aboutus/',views.aboutus,name="aboutus"),
    path('save_contact/',views.savecontact,name="save_contact"),
    path('products_filter/<cat_name>/',views.productsfilter,name="products_filter"),
    path('single_product/<int:proid>/',views.Singleproduct,name="single_product"),
    path('Signup/',views.loginspage,name="Signup"),
    path('',views.Signinpage,name="Signin"),
    path('save_signup/',views.save_signup,name="save_signup"),
    path('user_login/',views.User_login,name="user_login"),
    path('user_logout/',views.User_logout,name="user_logout"),
    path('savecart/',views.save_to_cart,name="savecart"),
    path('cart/',views.cart,name="cart"),
    path('removecart/<int:ctid>/',views.remove_cart,name="removecart"),
    path('checkout/',views.checkout,name="checkout"),
    path('save_checkout/', views.save_checkout, name="save_checkout"),
    path('payment/',views.payment_page,name="payment")
]