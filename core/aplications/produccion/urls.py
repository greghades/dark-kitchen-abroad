from django.urls import path
from .views import *
urlpatterns = [
    path('list_products/',List_product.as_view()),
    path('datail_product/<int:pk>',Detail_product.as_view()),
    path('create_product/',Create_product.as_view()),
    path('update_product/<int:pk>',Update_product.as_view()),
    path('delete_product/<int:pk>',Delete_product.as_view()),
]
