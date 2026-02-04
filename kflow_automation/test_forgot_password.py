# test_forgot_password.py
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

LOGIN_URL = "http://localhost:3000/kflow/pages/auth/login"


def react_type(driver, css_selector, value):
    driver.execute_script("""
        const input = document.querySelector(arguments[0]);
        if (!input) return;
        input.focus();
        input.value = arguments[1];
        input.dispatchEvent(new Event('input', { bubbles: true }));
        input.dispatchEvent(new Event('change', { bubbles: true }));
    """, css_selector, value)


def js_click(driver, css_selector):
    driver.execute_script("""
        const btn = document.querySelector(arguments[0]);
        if (btn) btn.click();
    """, css_selector)


def test_forgot_password_ui():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )
    wait = WebDriverWait(driver, 20)

    try:
        #  Open login page
        driver.get(LOGIN_URL)

        #  Click "Forgot password"
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(text(),'Forgot')]")
            )
        ).click()

        #  Wait for forgot-password page
        wait.until(EC.url_contains("forgot-password"))

        #  Enter email (React-safe)
        react_type(driver, "input[type='email']", "jagasri04@gmail.com")

        # Small pause to allow React re-render
        time.sleep(0.5)

        # JS click submit (NO stale issue)
        js_click(driver, "button[type='submit']")

        #  success UI
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(),'email')]")
            )
        )

        print(" Forgot Password UI test PASSED")

    finally:
        time.sleep(3)
        driver.quit()
