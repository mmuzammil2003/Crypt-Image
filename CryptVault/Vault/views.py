from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.views.generic import ListView, View
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse, Http404
from django.contrib.auth import login
from django.contrib.auth.hashers import check_password

from cryptography.fernet import InvalidToken

from .forms import LoginForm, RegistrationForm, UploadFileForm
from .models import UploadedFile


class RegistrationPage(FormView):
    template_name = 'Vault/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')  

    def form_valid(self, form):
        user=form.save() 
        login(self.request,user)
        return super().form_valid(form)


class LoginPage(LoginView):
    template_name = 'Vault/login.html'
    authentication_form = LoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


@method_decorator(login_required, name='dispatch')
class UploadFileView(FormView):
    template_name = 'Vault/home.html'
    form_class = UploadFileForm
    success_url = reverse_lazy('list_files') 

    def form_valid(self, form):
        uploaded_file = form.save(commit=False)
        uploaded_file.user = self.request.user
        uploaded_file.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ListFilesView(ListView):
    model = UploadedFile
    template_name = 'Vault/list_file.html'
    context_object_name = 'files'
    ordering = ['-uploaded_at']

    def get_queryset(self):
        return UploadedFile.objects.filter(user=self.request.user).order_by('-uploaded_at')




@method_decorator(login_required, name='dispatch')
def download_file(request, file_id):
    file = get_object_or_404(UploadedFile, id=file_id)

    if request.method == "POST":
        user_password = request.POST.get('password')
        
        # Replace this with your actual method for verifying passwords
        stored_password_hash = file.password_hash  # Assume you've stored the hashed password in the UploadedFile model
        
        if not check_password(user_password, stored_password_hash):
            return HttpResponse("Invalid password", status=403)

        try:
            # Decrypt the file content
            decrypted_content = file.decrypt()

            # Create the response with the decrypted file content
            response = HttpResponse(decrypted_content, content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename={file.file.name}'
            return response
        except InvalidToken:
            raise Http404("File cannot be decrypted with the provided password.")
    
    return render(request, 'Vault/password_prompt.html', {'file': file})
