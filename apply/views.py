from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from rest_framework.reverse import reverse

from account.models import User
from apply.forms import ApplyForm
from apply.models import Apply
from job.models import Job
from pro.models import Pro


# Create your views here.
class ApplyJobView(LoginRequiredMixin, View, FormMixin):
    template_name = 'apply.html'
    form_class = ApplyForm
    success_url = reverse_lazy('job:home')

    def get(self, request, slug):
        job = get_object_or_404(Job, slug=slug)

        if Apply.objects.filter(job=job, user=request.user).exists():
            messages.error(request, "You have already applied to this job.")
            return HttpResponseRedirect(reverse('job:detail', args=[slug]))

        if job.user == request.user:
            messages.error(request, "You cannot apply to the job you posted.")
            return HttpResponseRedirect(reverse('job:detail', args=[slug]))

        form = self.get_form()
        return render(request, self.template_name, {'form': form, 'job': job})

    def post(self, request, slug):
        job = get_object_or_404(Job, slug=slug)
        form = self.get_form()

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.job = job
            profile.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class StatusPostedView(LoginRequiredMixin, ListView):
    template_name = 'totalapplicant.html'
    context_object_name = 'job_count'

    def get_queryset(self):
        user = self.request.user
        jobs = Job.objects.filter(user=user)
        job_counts = []

        for job in jobs:
            count = Apply.objects.filter(job=job).count()
            job_counts.append((job, count))

        return job_counts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class ApplicantListView(LoginRequiredMixin, DetailView):
    model = Job
    template_name = 'applicants.html'
    context_object_name = 'job'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        job = self.object  # Fetches the Job object from the view
        apply_job = Apply.objects.filter(job=job)
        context['apply_job'] = apply_job
        context['user'] = self.request.user
        return context


class ProfileView(LoginRequiredMixin, DetailView):
    model = User  # Use the User model for fetching user details
    template_name = 'viewprofile.html'
    context_object_name = 'user'  # Context variable name to be used in template

    def get_object(self, queryset=None):
        user_id = self.kwargs.get('user_id')  # Get user_id from URL kwargs
        return get_object_or_404(User, id=user_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs.get('user_id')
        profile = get_object_or_404(Pro, user_id=user_id)
        context['profile'] = profile
        return context


class AppliedHistoryView(LoginRequiredMixin, ListView):
    model = Apply
    template_name = 'applied_history.html'
    context_object_name = 'applyjob'

    def get_queryset(self):
        return Apply.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


@login_required
def delete_applied(request,pk):
    dell = Apply.objects.get(id=pk)
    dell.delete()
    return HttpResponseRedirect('/applied_history')
