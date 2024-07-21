# For Generating URLs


from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.utils import timezone
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from rest_framework.generics import get_object_or_404

# Category Objects in Django
from job.models import Job, Category
from job.forms import JobForm


class HomePageView(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'job/home.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        now = timezone.now()
        return Job.objects.exclude(user=self.request.user).filter(job_validity__gte=now)


class ListViewJob(ListView):
    model = Job
    template_name = 'job/list.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        now = timezone.now()
        return Job.objects.exclude(user=self.request.user).filter(job_validity__gte=now)


class PostedListViewJob(ListView):
    model = Job
    template_name = 'job/postedjob_history.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        return Job.objects.filter(user=self.request.user)


class JobDetailView(DetailView):
    model = Job
    template_name = 'job/detail.html'
    context_object_name = 'job'
    slug_url_kwarg = 'slug'  # Specify the slug URL keyword

    def get_object(self, queryset=None):
        slug = self.kwargs.get(self.slug_url_kwarg)
        return get_object_or_404(Job, slug=slug)


class JobCreateView(SuccessMessageMixin, CreateView):
    model = Job
    template_name = 'job/form.html'
    form_class = JobForm
    success_url = reverse_lazy('job:list')
    extra_context = {'what': 'Create'}
    success_message = "Job created successfully."

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class JobUpdateView(SuccessMessageMixin, UpdateView):
    model = Job
    template_name = 'job/form.html'
    form_class = JobForm
    success_url = reverse_lazy('job:list')
    extra_context = {'what': 'Update'}
    success_message = "Job updated successfully."


class JobRemoveView(DeleteView):
    model = Job
    template_name = 'job/remove.html'
    success_url = reverse_lazy('job:list')


class JobSearchView(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'job/search_result.html'
    context_object_name = 'results'

    def get_queryset(self):
        query = self.request.GET.get('q')
        current_time = timezone.now()
        if query:
            return Job.objects.filter(
                (Q(job_title__icontains=query) |
                 Q(job_description__icontains=query)) &
                Q(job_validity__gt=current_time)
            )
        return Job.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context


