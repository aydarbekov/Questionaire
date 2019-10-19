from django.contrib import admin
from django.urls import path

from webapp.views.poll_views import IndexView, PollView, PollCreateView, PollUpdateView, PollDeleteView, PollAnswerView
from webapp.views.choise_views import ChoiseForPollCreateView, ChoiceUpdateView, ChoiceDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('poll/<int:pk>/', PollView.as_view(), name='poll_view'),
    path('poll/add/', PollCreateView.as_view(), name='poll_create'),
    path('poll/<int:pk>/edit/', PollUpdateView.as_view(), name='poll_update'),
    path('poll/<int:pk>/delete/', PollDeleteView.as_view(), name='poll_delete'),
    path('poll/<int:pk>/add-choise/', ChoiseForPollCreateView.as_view(), name='poll_choice_create'),
    path('choice/<int:pk>/edit/', ChoiceUpdateView.as_view(), name='choice_update'),
    path('choice/<int:pk>/delete/', ChoiceDeleteView.as_view(), name='choice_delete'),
    path('poll/<int:pk>/answer', PollAnswerView.as_view(), name='poll_answer'),

]
