from django.shortcuts import render
from multiprocessing import context, reduction
from os import supports_bytes_environ
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, CreateView, FormView, DetailView, ListView
from django.urls import reverse_lazy
from django.urls.base import reverse

from .models import *
from django.core.paginator import Paginator
from django.db.models import Q
from django.views import generic
from django.contrib.auth import authenticate, login, logout

class HomeView(TemplateView):
    template_name = 'catalogo/home.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        pesquisa = self.request.GET.get('pesquisaProduto')
        if pesquisa:
            produtos = Produto.objects.filter(Q(nome__icontains=pesquisa) | Q(descricao__icontains=pesquisa)).order_by('categoria__nome')   
            # results = Categoria.objects.filter(Q(produto__nome__icontains=pesquisa) | Q(produto__descricao__icontains=pesquisa))   
            # print(results.query)
        else:
            produtos = Produto.objects.all().order_by('categoria__nome')       
        
        categorias = Categoria.objects.all().order_by('nome')
        context['todasCategorias']=categorias
        context['produtos']=produtos
        return context

class ProdutoDetalheView(TemplateView):
    template_name = 'catalogo/produtoDetalhe.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        prod_id = self.kwargs['id']
        produto = Produto.objects.get(id = prod_id)   

        
        context['produto']=produto
        return context