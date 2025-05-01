from django.db import models
from django.contrib.auth.models import User
from cryptography.fernet import Fernet
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
from django.contrib.auth.hashers import make_password

# Generate a key — for real projects, store this securely
key = Fernet.generate_key()
cipher_suite = Fernet(key)

class EncryptedFileSystemStorage(FileSystemStorage):
    def _save(self, name, content):
        # Read original content
        original_data = content.read()
        
        # Encrypt it
        encrypted_data = cipher_suite.encrypt(original_data)
        
        # Wrap in ContentFile (file-like object)
        encrypted_file = ContentFile(encrypted_data)
        
        # Save as usual
        return super()._save(name, encrypted_file)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class UploadedFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    file = models.FileField(upload_to='uploads/', storage=EncryptedFileSystemStorage())
    uploaded_at = models.DateTimeField(auto_now_add=True)
    password_hash = models.CharField(max_length=255)  # Store the hashed password

    def __str__(self):
        return self.file.name

    def decrypt(self):
        with self.file.open('rb') as f:
            encrypted_data = f.read()
            return cipher_suite.decrypt(encrypted_data)

    def set_password(self, raw_password):
        """Hash the password and save the hash."""
        self.password_hash = make_password(raw_password)