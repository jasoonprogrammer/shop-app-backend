from django.urls import path
from . import views
urlpatterns = [
    path("category/create", views.CategoryCreateAPI.as_view()),
    path("category/list", views.CategoryListAPI.as_view()),
    path("category/update/<int:pk>", views.CategoryUpdateAPI.as_view()),
    path("product/list", views.ProductListAPI.as_view()),
    path("product/create", views.ProductCreateAPI.as_view()),
    path("product/update/<int:pk>", views.ProductUpdateAPI.as_view()),
    path("price_update/create", views.PriceUpdateCreateAPI.as_view()),
    path("price_update/update", views.PriceUpdateAPI.as_view()),
    path("price_update/list", views.PriceUpdateListAPI.as_view()),
    
    path("sale/create", views.SaleCreateAPI.as_view()),
    path("sale/update", views.SaleUpdateAPI.as_view()),
    path("sale/list", views.SaleListAPI.as_view()),
    path("transaction/detail/<int:pk>", views.TransactionRetrieveAPI.as_view()),
    path("transaction/list", views.TransactionListAPI.as_view()),
    path("transaction/create", views.TransactionCreateAPI.as_view()),
    

]