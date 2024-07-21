from django.urls import path
from . import views
from .views import ApplyJobView, StatusPostedView, ApplicantListView, ProfileView, AppliedHistoryView

app_name = 'apply'

urlpatterns = [
    path('apply/<slug:slug>/', ApplyJobView.as_view(), name='apply_job'),
    path('total_applicant/', StatusPostedView.as_view(), name='total_applicant'),
    path('applicants/<int:pk>/', ApplicantListView.as_view(), name='applicants'),
    path('profile/<int:user_id>/', ProfileView.as_view(), name='profile_view'),
    path('applied_history/', AppliedHistoryView.as_view(), name='applied_history'),
    path('delete_applied/<int:pk>', views.delete_applied, name='delete_applied'),

    # Add other paths as needed
]
