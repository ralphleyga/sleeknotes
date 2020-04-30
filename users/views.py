from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    UpdateView,
    )
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from .models import User


class IndexView(TemplateView):
    template_name = 'index.html'
