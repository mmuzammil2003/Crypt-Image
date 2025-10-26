from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from django.contrib.auth.models import User
import tempfile, os, time

class TestInvalidDownlaod(StaticLiveServerTestCase):
    def setUp(self):
        from django.core.files.base import ContentFile
        from Vault.models import UploadedFile
        from django.contrib.auth.hashers import make_password
        from django.contrib.auth.models import User
        from django.conf import settings

        self.user=User.objects.create_user(username="user1",password="strongPass123!",email="test@example.com")

        self.file=UploadedFile.objects.create(
            user=self.user,
            password_hash=make_password("correctpass"),
            file=ContentFile(b"Secret file content",name="test.txt")
        )

        chrome_options=Options()
        chrome_options.add_argument("--headless")
        service=Service()
        self.driver=webdriver.Chrome(service=service,options=chrome_options)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def test_invalid_password_triggers_error(self):
        # First login
        self.driver.get(f"{self.live_server_url}/")
        time.sleep(1)
        
        assert "Login" in self.driver.page_source
        
        self.driver.find_element(By.NAME,"username").send_keys("user1")
        self.driver.find_element(By.NAME,"password").send_keys("strongPass123!")
        self.driver.find_element(By.CSS_SELECTOR,"form button[type='submit']").click()
        time.sleep(3)
        
        self.driver.get(f"{self.live_server_url}/files/")
        time.sleep(3)
        
        assert "Secure File Vault" in self.driver.page_source
        
        password_input = self.driver.find_element(By.CSS_SELECTOR,"input[type='password']")
        password_input.send_keys("wrongpassword")
        
        download_btn = self.driver.find_element(By.CSS_SELECTOR,"button.download-btn")
        download_btn.click()
        time.sleep(3)

        assert "Invalid password" in self.driver.page_source    
    