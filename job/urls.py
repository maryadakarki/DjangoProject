from django.urls import path
from job.views import (
    ListViewJob, JobCreateView, JobUpdateView, JobRemoveView, JobDetailView, HomePageView, PostedListViewJob,
    JobSearchView
)

app_name = 'job'

urlpatterns = [
    path('job/list', ListViewJob.as_view(), name='list'),
    path('job/create/', JobCreateView.as_view(), name='create'),
    path('job/update/<slug:slug>', JobUpdateView.as_view(), name='update'),
    path('job/remove/<slug:slug>', JobRemoveView.as_view(), name='remove'),
    path('job/detail/<slug:slug>/', JobDetailView.as_view(), name='detail'),
    path('', HomePageView.as_view(), name='home'),
    path('job/postedjoblist/', PostedListViewJob.as_view(), name='postedjoblist'),
    path('job_search/', JobSearchView.as_view(), name='job_search'),

]
