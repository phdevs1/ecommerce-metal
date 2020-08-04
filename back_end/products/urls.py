from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.auth_login, name='authentication'),
    path('logout/',views.logout,  name='logout1'),
    path('product/', views.hello_world, name='producto'),
    path('product1/', views.ProductList.as_view(), name='producto1'),
    path('newproudct/',views.new_product, name='newproduct'),
    path('productdetail/<int:pk>',views.ProductDetail.as_view(), name='detail1'),
    path('productListAPI',views.ProductListAPI.as_view(),name='product_list_API'),
]
