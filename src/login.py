from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import sys

def login(driver) :
    print("login initialisé...")
    driver.get("https://www.mobilax.fr/login")
    email_input = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
    email_input.send_keys("louis.lantiez4@icloud.com")

    # Remplissage du mot de passe
    password_input = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
    password_input.send_keys("Google59")

    # Appui sur le bouton "Se connecter"
    connect_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Se connecter')]")
    connect_button.click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".products")))
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    print("login fait ✅")
    return driver