from django.urls import path
from .views import RegistrationPage, LoginPage, UploadFileView, ListFilesView

urlpatterns = [
    path('register/', RegistrationPage.as_view(), name='register'),
    path('login/', LoginPage.as_view(), name='login'),
    path('home/', UploadFileView.as_view(), name='home'),
    path('files/', ListFilesView.as_view(), name='list_files'),
]
