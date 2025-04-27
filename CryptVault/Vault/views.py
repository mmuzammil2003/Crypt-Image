from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views import View
from .forms import LoginForm, RegistrationForm, UploadFileForm
from .models import UploadedFile


class RegistrationPage(FormView):
    template_name = 'Vault/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('home')  

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class LoginPage(LoginView):
    template_name = 'Vault/login.html'
    authentication_form = LoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class UploadFileView(FormView):
    template_name = 'Vault/home.html'
    form_class = UploadFileForm
    success_url = reverse_lazy('list_files') 

    def form_valid(self, form):
        uploaded_file = form.save(commit=False)
        uploaded_file.user = self.request.user 
        uploaded_file.save()
        return super().form_valid(form)


class ListFilesView(ListView):
    model = UploadedFile
    template_name = 'Vault/list_file.html'
    context_object_name = 'files'
    ordering = ['-uploaded_at']

    def get_queryset(self):
        return UploadedFile.objects.filter(user=self.request.user).order_by('-uploaded_at')



class DownloadFileView(View):
    def get(self, request, file_id):
        try:
            file = UploadedFile.objects.get(id=file_id, user=request.user)
            decrypted_data = file.decrypt()  # Decrypt the file
            response = HttpResponse(decrypted_data, content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename={file.file.name}'
            return response
        except UploadedFile.DoesNotExist:
            return HttpResponse('File not found or you do not have permission to download it', status=403)

