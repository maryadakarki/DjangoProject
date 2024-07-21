from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from pro.forms import ProForm
from pro.models import Pro


# Create your views here.


def custom_login(request):
    if not Pro.objects.filter(user=request.user).exists():
        return redirect('pro:create')
    else:
        return redirect('job:home')


class ProCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Pro
    template_name = 'form_c.html'
    form_class = ProForm
    success_url = reverse_lazy('pro:profile')
    extra_context = {'what': 'Create'}
    success_message = "Profile created successfully."

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProUpdateView(SuccessMessageMixin, UpdateView):
    model = Pro
    template_name = 'form_c.html'
    form_class = ProForm
    success_url = reverse_lazy('pro:profile')
    extra_context = {'what': 'Update'}
    success_message = "Profile updated successfully."

    def get_object(self, queryset=None):
        # Assuming the user can have only one profile
        return Pro.objects.get(user=self.request.user)


@login_required
def profile(request):
    user = request.user
    profile = user.pro
    return render(request, 'profile.html', {'user': user, 'profile': profile})



# @login_required
# def createprofile(request):
#     if request.method == 'POST':
#         form = ProForm(request.POST, request.FILES)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.user = request.user
#             profile.save()
#             return redirect('home')
#     else:
#         form = ProForm()
#     return render(request, 'createprofile.html', {'form': form})