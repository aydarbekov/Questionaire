from django.forms import Form
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View

from webapp.forms import PollForm
from webapp.models import Poll
# from webapp.forms import TaskForm, ProjectTaskForm, SimpleSearchForm
# from webapp.views.base_views import MassDeleteView
from django.db.models import Q
from django.utils.http import urlencode


class IndexView(ListView):
    template_name = 'poll/index.html'
    context_object_name = 'polls'
    model = Poll
    ordering = '-created_at'
    paginate_by = 5
    paginate_orphans = 1

    # def get(self, request, *args, **kwargs):
    #     self.form = self.get_search_form()
    #     self.search_value = self.get_search_value()
    #     return super().get(request, *args, **kwargs)

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(object_list=object_list, **kwargs)
    #     context['form'] = self.form
    #     if self.search_value:
    #         context['query'] = urlencode({'search': self.search_value})
    #     return context

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     if self.search_value:
    #         query = Q(description__icontains=self.search_value) | Q(full_descr__icontains=self.search_value)
    #         queryset = queryset.filter(query)
    #     return queryset

    # def get_search_form(self):
    #     return SimpleSearchForm(self.request.GET)

    # def get_search_value(self):
    #     if self.form.is_valid():
    #         return self.form.cleaned_data['search']
    #     return None


class PollView(DetailView):
    template_name = 'poll/poll.html'
    pk_url_kwarg = 'pk'
    model = Poll


class PollCreateView(CreateView):
    template_name = 'poll/create.html'
    model = Poll
    form_class = PollForm

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollUpdateView(UpdateView):
    model = Poll
    template_name = 'poll/update.html'
    form_class = PollForm
    context_object_name = 'poll'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollDeleteView(DeleteView):
    template_name = 'poll/delete.html'
    model = Poll
    context_object_name = 'poll'
    success_url = reverse_lazy('index')