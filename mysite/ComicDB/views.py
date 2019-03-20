from django.shortcuts import render

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Comics


class ComicsList(ListView): 
    model = Comics
	
class ComicsDetails(DetailView): 
    model = Comics
	
class ComicsCreate(CreateView): 
	model = Comics
	fields = ['title', 'issue', 'publisher']
	success_url = reverse_lazy('comics_list')
	
class ComicsUpdate(UpdateView): 
	model = Comics
	fields = ['title', 'issue', 'publisher']
	success_url = reverse_lazy('comics_list')
	
class ComicsDelete(DeleteView): 
	model = Comics
	success_url = reverse_lazy('comics_list')
