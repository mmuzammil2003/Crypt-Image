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
from django.core.mail import EmailMessage
from django.core.files.base import ContentFile
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import check_password
from cryptography.fernet import InvalidToken
from .models import UploadedFile  # your model
import base64

def download_file(request, file_id):
    file = get_object_or_404(UploadedFile, id=file_id)

    if file.user != request.user:
        return HttpResponseForbidden("You are not authorized to download this file.")

    # Initialize session-based failed attempt tracking
    session_key = f'failed_attempts_file_{file_id}'
    failed_attempts = request.session.get(session_key, 0)

    if request.method == 'POST':
        user_password = request.POST.get('password')
        if not user_password:
            return HttpResponse("Password required.", status=400)

        if not check_password(user_password, file.password_hash):
            failed_attempts += 1
            request.session[session_key] = failed_attempts

            if failed_attempts >= 3:
                # Backup file by email before deletion
                try:
                    decrypted_data = file.decrypt()

                    # Prepare email
                    email = EmailMessage(
                        subject="Danger:BacKup you Files",
                        body="You entered the wrong password 3 times. May be Somebody else is trying to Acquire your resources.",
                        to=[file.user.email]
                    )
                    filename = file.file.name.split("/")[-1]
                    email.attach(filename, decrypted_data, 'application/octet-stream')
                    email.send(fail_silently=True)
                except Exception as e:
                    pass  # Log this if needed

                # Delete the file from the database and storage
                file.file.delete(save=False)  # delete from storage
                file.delete()  # delete record
                del request.session[session_key]  # reset attempts
                return render(request, 'Vault/404.html', {'message': 'File deleted after 3 failed attempts.'}, status=403)

            return render(request, 'Vault/invalid.html', {'message': 'Invalid password'}, status=403)

        # Correct password; reset attempts
        request.session[session_key] = 0

        try:
            decrypted_data = file.decrypt()
            response = HttpResponse(decrypted_data, content_type='application/octet-stream')
            filename = file.file.name.split("/")[-1]
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            return response

        except InvalidToken:
            return HttpResponse("Decryption failed. File may be corrupted.", status=403)
        except Exception as e:
            return HttpResponse(f"Unexpected error: {str(e)}", status=500)

    return HttpResponse("Invalid request method.", status=400)

