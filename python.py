import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Charger les liens depuis un fichier JSON
with open('links.json', 'r') as f:
    data = json.load(f)
    links_to_open = data['links_to_open']

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(300, 300)

wait = WebDriverWait(driver, 12)

for link in links_to_open:
    try:
        driver.get(link)
        link_element = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "ACCÉDER AU LIEN")))

        link_element.click()

        window_handles = driver.window_handles
        if len(window_handles) > 1:
            driver.switch_to.window(window_handles[-1])
            driver.close()
            driver.switch_to.window(window_handles[0])

        time.sleep(20)

    except Exception as e:
        print(f"Erreur lors de l'ouverture du lien {link}: {e}")

driver.quit()
