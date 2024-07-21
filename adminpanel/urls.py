from django.urls import path
from .views import AdminView, JobReportView, UserListView, ListViewCategory, CategoryCreateView, CategoryUpdateView, \
    CategoryRemoveView

app_name = 'adminpanel'

urlpatterns = [
    path('admin_panel/', AdminView.as_view(), name='admin_panel'),
    path('job_report/', JobReportView.as_view(), name='job_report'),
    path('users/', UserListView.as_view(), name='users'),

    path('list_c/', ListViewCategory.as_view(), name='list_c'),
    path('create_c/', CategoryCreateView.as_view(), name='create_c'),
    path('update_c/<slug:slug>', CategoryUpdateView.as_view(), name='update_c'),
    path('remove_c/<slug:slug>', CategoryRemoveView.as_view(), name='remove_c'),

]
