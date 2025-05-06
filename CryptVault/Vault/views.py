from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth import login
from django.contrib.auth.hashers import check_password
from cryptography.fernet import InvalidToken

from .forms import LoginForm, RegistrationForm, UploadFileForm
from .models import UploadedFile

# ----------------- Registration -----------------
class RegistrationPage(FormView):
    template_name = 'Vault/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')  

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

# ----------------- Login -----------------
class LoginPage(LoginView):
    template_name = 'Vault/login.html'
    authentication_form = LoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

# ----------------- File Upload -----------------
@method_decorator(login_required, name='dispatch')
class UploadFileView(FormView):
    template_name = 'Vault/home.html'
    form_class = UploadFileForm
    success_url = reverse_lazy('list_files')

    def form_valid(self, form):
        uploaded_file = form.save(commit=False)
        uploaded_file.user = self.request.user
        
        # Hash the password before saving
        password = self.request.POST.get('password')  # Get password from form
        if password:
            uploaded_file.set_password(password)  # Set the password hash for this file
        uploaded_file.save()
        
        return super().form_valid(form)

# ----------------- File Listing -----------------
@method_decorator(login_required, name='dispatch')
class ListFilesView(ListView):
    model = UploadedFile
    template_name = 'Vault/list_file.html'
    context_object_name = 'files'

    def get_queryset(self):
        return UploadedFile.objects.filter(user=self.request.user).order_by('-uploaded_at')

# ----------------- File Download -----------------
def download_file(request, file_id):
    # Retrieve the file object using the file_id from the URL
    file = get_object_or_404(UploadedFile, id=file_id)

    # Check if the user is authorized to download this file
    if file.user != request.user:
        return HttpResponseForbidden("You are not authorized to download this file.")

    # If the request method is POST, process the password
    if request.method == 'POST':
        user_password = request.POST.get('password')
        if not user_password:
            return HttpResponse("Password required.", status=400)

        # Check if the provided password is correct
        if not check_password(user_password, file.password_hash):
            return HttpResponse("Invalid password", status=403)

        try:
            # Attempt to decrypt the file
            decrypted_data = file.decrypt()

            # Return the decrypted file as a response
            response = HttpResponse(decrypted_data, content_type='application/octet-stream')
            filename = file.file.name.split("/")[-1]
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            return response

        except InvalidToken:
            return HttpResponse("Decryption failed. File may be corrupted.", status=403)
        except Exception as e:
            return HttpResponse(f"Unexpected error: {str(e)}", status=500)

    return HttpResponse("Invalid request method.", status=400)
