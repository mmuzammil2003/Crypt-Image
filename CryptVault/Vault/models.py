from django.db import models
from django.contrib.auth.models import User
from cryptography.fernet import Fernet
from django.core.files.storage import FileSystemStorage

key = Fernet.generate_key()
cipher_suite = Fernet(key)

class EncryptedFileSystemStorage(FileSystemStorage):
    def _save(self, name, content):
        encrypted_content = cipher_suite.encrypt(content.read())
        return super()._save(name, encrypted_content)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class UploadedFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  
    file = models.FileField(upload_to='uploads/', storage=EncryptedFileSystemStorage())
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name

    def decrypt(self):
        with self.file.open('rb') as f:
            encrypted_data = f.read()
            return cipher_suite.decrypt(encrypted_data)

