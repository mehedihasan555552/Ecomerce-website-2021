from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Index, name='index'),
    path('store/', views.Store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('remove_cart/<int:product_id>/<int:cart_item_id>/', views.remove_cart, name='remove_cart'),
    path('remove_cart_item/<int:product_id>/<int:cart_item_id>/', views.remove_cart_item, name='remove_cart_item'),

    path('search/', views.search, name='search'),
    path('login/', views.userlogin, name='login'),
    path('register/', views.usersignup, name='register'),
    path('logout/', views.userlogout,name='logout'),
    path('dashboard/', views.Dashboard,name='dashboard'),
    path('checkout/', views.checkout,name='checkout'),
    path('place-order/', views.Place_Order,name='place_order'),
    path('payments/', views.payments,name='payments'),
    path('order_complete/', views.order_complete,name='order_complete'),
    path('submit_review/<int:product_id>/', views.submit_review,name='submit_review'),
    path('my_orders/', views.my_orders,name='my_orders'),
    path('edit_profile/', views.edit_profile,name='edit_profile'),
    path('change_password/', views.change_password,name='change_password'),
    path('order_detail/<int:order_id>/', views.order_detail,name='order_detail'),
    



    path('category/<slug:category_slug>/', views.Store, name='products_by_category'),
    path('product-details/<slug:category_slug>/<slug:product_slug>/', views.Product_Detail, name='product_detail'),
    
    
    

    
   
      
]
