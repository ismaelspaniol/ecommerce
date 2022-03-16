from django.urls import path
from .views import *


app_name = 'catalogo'
urlpatterns = [
     path('', HomeView.as_view(), name='home'),
     path('produto/<int:id>/', ProdutoDetalheView.as_view(), name='produtoDetalhe'),
     
]