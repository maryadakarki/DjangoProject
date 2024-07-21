from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView
from rest_framework.reverse import reverse_lazy

from adminpanel.forms import CategoryForm
from apply.models import Apply
from job.models import Job, Category
from pro.models import Pro


class AdminView(LoginRequiredMixin, TemplateView):
    template_name = 'admin.html'


class JobReportView(LoginRequiredMixin, TemplateView):
    template_name = 'jobreport.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        jobs = Job.objects.all()
        counts = [Apply.objects.filter(job_id=job.id).count() for job in jobs]
        jc = zip(jobs, counts)
        context['user'] = user
        context['jc'] = jc
        return context


class UserListView(LoginRequiredMixin, ListView):
    model = Pro
    template_name = 'users.html'
    context_object_name = 'users'

# For Categories


class ListViewCategory(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'list.html'
    context_object_name = 'categories'


class CategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Category
    template_name = 'form_c.html'
    form_class = CategoryForm
    success_url = reverse_lazy('adminpanel:list_c')
    extra_context = {'job': 'Create'}
    success_message = "Category created successfully."


class CategoryUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Category
    template_name = 'form_c.html'
    form_class = CategoryForm
    success_url = reverse_lazy('adminpanel:list_c')
    extra_context = {'job': 'Update'}
    success_message = "Category updated successfully."


class CategoryRemoveView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'remove.html'
    success_url = reverse_lazy('adminpanel:list_c')
