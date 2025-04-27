from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth import login
from .forms import LoginForm, RegistrationForm

class RegistrationPage(FormView):
    template_name='Vault/registration.html'
    form_class=RegistrationForm
    success_url=reverse_lazy('login')
    
    def form_valid(self,form):
        user=form.save()
        login(self.request,user)
        return super().form_valid(form)
    
class LoginPage(LoginView):
    template_name='Vault/login.html'
    authentication_form=LoginForm
    redirect_authenticated_user=True

    def get_success_url(self):
        return reverse_lazy('home')
    
from django.views.generic import FormView, ListView
from django.urls import reverse_lazy
from .models import UploadedFile
from django import forms

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']

class UploadFileView(FormView):
    template_name = 'Vault/home.html'
    form_class = UploadFileForm
    success_url = reverse_lazy('list_files')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ListFilesView(ListView):
    model = UploadedFile
    template_name = 'Vault/list_file.html'
    context_object_name = 'files'
    ordering = ['-uploaded_at']

# Vault/views.py

from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django import forms

from .forms import LoginForm, RegistrationForm
from .models import UploadedFile

# --- Authentication Views ---

class RegistrationPage(FormView):
    template_name = 'Vault/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('home')  # after registration, go to home

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

# --- File Upload and List Views ---

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']

class UploadFileView(FormView):
    template_name = 'Vault/home.html'  # Upload page template
    form_class = UploadFileForm
    success_url = reverse_lazy('list_files')  # After upload, go to list

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ListFilesView(ListView):
    model = UploadedFile
    template_name = 'Vault/list_file.html'  # corrected your path here
    context_object_name = 'files'
    ordering = ['-uploaded_at']

