from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.contrib.auth.models import User
import tempfile, os, time

class TestFileUpload(StaticLiveServerTestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="StrongPass123!")
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        service = Service()
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def login(self):
        self.driver.get(f"{self.live_server_url}/")
        self.driver.find_element(By.NAME, "username").send_keys("testuser")
        self.driver.find_element(By.NAME, "password").send_keys("StrongPass123!")
        self.driver.find_element(By.CSS_SELECTOR, "form button[type='submit']").click()
        time.sleep(2)
        self.assertIn("/home", self.driver.current_url, "Login failed — still on login page")

    def test_file_upload(self):
        self.login()
        
        # Navigate to home page for file upload
        self.driver.get(f"{self.live_server_url}/home/")
        time.sleep(2)

        tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.txt')
        tmp_file.write(b"sample data for encryption test")
        tmp_file.close()

        file_input = self.driver.find_element(By.NAME, "file")
        file_input.send_keys(tmp_file.name)
        
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys("1234")
        
        submit_btn = self.driver.find_element(By.CSS_SELECTOR, "form button[type='submit']")
        submit_btn.click()

        WebDriverWait(self.driver, 10).until(EC.url_contains("/files/"))
        self.assertIn("/files/", self.driver.current_url)
        assert "Secure File Vault" in self.driver.page_source

        os.remove(tmp_file.name)
