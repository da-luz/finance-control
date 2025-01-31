from django.forms import DateTimeInput
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView

from control.models import Category, Transaction


class TransactionsListView(LoginRequiredMixin, ListView):
    template_name="control/list.html"
    model=Transaction

class TransactionUpdateView(LoginRequiredMixin, UpdateView):
    template_name="control/update.html"
    model=Transaction
    fields=["category", "amount", "description", "created_at"]
    success_url="/"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['created_at'].widget = DateTimeInput(format=("%Y-%m-%d"), attrs={"type": "date"})
        return form   

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    template_name="control/update.html"
    model=Category
    fields=["name", "flow",]
    success_url="/"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['created_at'].widget = DateTimeInput(format=("%Y-%m-%d"), attrs={"type": "date"})
        return form

class TransactionCreateView(LoginRequiredMixin, CreateView):
    template_name="control/create.html"
    model=Transaction
    fields=["category", "amount", "description", "created_at"]
    success_url="/"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['created_at'].widget = DateTimeInput(format=("%Y-%m-%d"), attrs={"type": "date"})
        return form

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
class CategoryCreateView(LoginRequiredMixin, CreateView):
    template_name="control/create.html"
    model=Category
    fields=["name", "flow",]
    success_url="/"
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
