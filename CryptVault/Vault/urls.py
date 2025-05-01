from django.urls import path
from .views import RegistrationPage, LoginPage, UploadFileView, ListFilesView
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('register/', RegistrationPage.as_view(), name='register'),
    path('', LoginPage.as_view(), name='login'),
    path('home/', UploadFileView.as_view(), name='home'),
    path('files/', ListFilesView.as_view(), name='list_files'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('file/download/<int:file_id>/', views.download_file, name='download_file'),

]
