from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

class TEstUserSUthFlow(StaticLiveServerTestCase):
    def setUp(self):
        chrome_options=Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        service=Service()
        self.driver=webdriver.Chrome(service=service,options=chrome_options)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()
    
    def test_user_registration_and_login(self):
        driver=self.driver

        driver.get(f"{self.live_server_url}/register")
        time.sleep(1)
        
      
        assert "Register" in driver.page_source
        
        driver.find_element(By.NAME,"username").send_keys("testuser")
        driver.find_element(By.NAME,"email").send_keys("test@example.com")
        driver.find_element(By.NAME,"password1").send_keys("StrongPass123!")
        driver.find_element(By.NAME,"password2").send_keys("StrongPass123!")
        driver.find_element(By.CSS_SELECTOR,"form button[type='submit']").click()
        time.sleep(3)

        # After registration, user should be redirected to login page
        # Now test login
        driver.get(f"{self.live_server_url}")
        time.sleep(1)
        
        # Check if we're on the login page
        assert "Login" in driver.page_source
        
        driver.find_element(By.NAME,"username").send_keys("testuser")
        driver.find_element(By.NAME,"password").send_keys("StrongPass123!")
        driver.find_element(By.CSS_SELECTOR,"form button[type='submit']").click()
        time.sleep(3)

        # Check if we're redirected to home page
        self.assertIn("/home",driver.current_url)
        assert "upload a File" in driver.page_source
                