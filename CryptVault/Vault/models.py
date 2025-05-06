from django.db import models
from django.contrib.auth.models import User
from cryptography.fernet import Fernet
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
from django.contrib.auth.hashers import make_password

from django.conf import settings

# Encryption setup
cipher_suite = Fernet(settings.ENCRYPTION_KEY)

# Custom file storage class to handle encrypted files
class EncryptedFileSystemStorage(FileSystemStorage):
    def _save(self, name, content):
        original_data = content.read()
        encrypted_data = cipher_suite.encrypt(original_data)
        encrypted_file = ContentFile(encrypted_data)
        return super()._save(name, encrypted_file)

# UserProfile model for extending User model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

# UploadedFile model for storing encrypted files and password hashes
class UploadedFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    file = models.FileField(upload_to='uploads/', storage=EncryptedFileSystemStorage())
    uploaded_at = models.DateTimeField(auto_now_add=True)
    password_hash = models.CharField(max_length=255)

    def __str__(self):
        return self.file.name

    # Decrypt the file content
    def decrypt(self):
        with self.file.open('rb') as f:
            encrypted_data = f.read()
            return cipher_suite.decrypt(encrypted_data)

    # Set password for the file (hashed)
    def set_password(self, raw_password):
        self.password_hash = make_password(raw_password)
