from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuration du mode headless pour ne pas afficher la fenêtre
options = Options()
options.headless = True

# Initialiser le navigateur
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# Ouvrir la page Google
driver.get("https://www.google.com")

# Afficher l'URL actuelle pour confirmer que la page Google est bien ouverte
print("Page ouverte:", driver.current_url)

# Ajouter un délai pour observer le comportement du bot
time.sleep(5)

# Fermer le navigateur
driver.quit()
