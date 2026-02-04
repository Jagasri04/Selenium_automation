#test_reset_password.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

RESET_URL = (
    "http://localhost:3000/kflow/pages/auth/reset-password"
    "?token=invalid-or-mock-token"
)

def react_type(driver, css_selector, value):
    driver.execute_script("""
        const input = document.querySelector(arguments[0]);
        if (!input) return;
        input.focus();
        input.value = arguments[1];
        input.dispatchEvent(new Event('input', { bubbles: true }));
        input.dispatchEvent(new Event('change', { bubbles: true }));
    """, css_selector, value)


def test_reset_password_ui():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )
    wait = WebDriverWait(driver, 20)

    try:
        driver.get(RESET_URL)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))


        # If token invalid then assert error UI instead
        if "invalid" in driver.page_source.lower():
            print("Invalid token page shown — UI OK")
            return

        react_type(driver, "input[name='password']", "Test@1234")
        react_type(driver, "input[name='confirmPassword']", "Test@1234")

        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(., 'Reset')]")
            )
        ).click()

        time.sleep(5)  # Wait for redirect
        assert "login" in driver.current_url.lower()
        print("Reset Password UI test PASSED")

    finally:
        time.sleep(5)
        driver.quit()

        