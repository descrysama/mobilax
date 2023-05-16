
from webinit_ import initBrowser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys


def find_element_with_retry(driver, target, url):
    while True:
        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, target)))
            return
        except:
            print("Element not found, retrying...")
            driver.get(url)
            find_element_with_retry(driver, target, url)
            continue

def single_page(url_array, results, cookie) :
    if(len(url_array) < 1) : 
        return
    
    total_items = []
    driver = initBrowser(True)
    driver.get("https://www.mobilax.fr")
    driver.execute_script("document.cookie='" + cookie + "; path=/; domain=www.mobilax.fr; secure=false; sameSite=Strict;'")

    for telephone_index, category_page in enumerate(url_array):
        try:
            
            # Naviguer vers la page de la catégorie
            driver.get(category_page)
            ##os.system("cls")
            print(" ---------- " ,telephone_index + 1, " / " , len(url_array)," ---------- ")
            # Attendre que les produits soient chargés
            find_element_with_retry(driver, "a.app-product-tile", category_page)

            # Récupérer les liens de tous les produits de la catégorie
            product_elements = driver.find_elements(By.CSS_SELECTOR, "a.app-product-tile")
            product_links = [el.get_attribute('href') for el in product_elements]

            for produit_index, product_link in enumerate(product_links):

                # Naviguer vers la page du produit
                driver.get(product_link)
                item = ["",""]

                find_element_with_retry(driver, "section.name-container p", product_link)
                driver.execute_script("window.stop();")
                reference_element = driver.find_element(By.CSS_SELECTOR, "section.name-container p")

                find_element_with_retry(driver, "div.current-price p.value.app-typo-h4", product_link)
                prix_element = driver.find_element(By.CSS_SELECTOR, "div.current-price p.value.app-typo-h4")
                driver.execute_script("window.stop();")
                reference_element_text = reference_element.text.replace("RÉF: ", "")
                prix_element_text = prix_element.text.replace(" € HT", "")
                
                item[0] = reference_element_text
                item[1] = prix_element_text
                print(produit_index + 1, " / " , len(product_links), " produits")
                total_items.append(item)
        except:
            print("thread error")
            driver.quit()
            return        
    driver.quit()
    results.extend(total_items)