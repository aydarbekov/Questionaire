from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import PollChoiseForm, ChoiceForm
from webapp.models import Poll, Choice, Answer


class AnswersView(ListView):
    template_name = 'answer/list.html'
    context_object_name = 'answers'
    model = Answer
    ordering = '-created_at'
    paginate_by = 5
    paginate_orphans = 1