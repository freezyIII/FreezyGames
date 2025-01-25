from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configuration de l'option headless (sans interface graphique)
chrome_options = Options()
chrome_options.add_argument('--headless')  # Mode sans tête
chrome_options.add_argument('--no-sandbox')  # Pour éviter des problèmes de sécurité
chrome_options.add_argument('--disable-dev-shm-usage')  # Pour éviter des erreurs liées à l'espace mémoire

# Chemin vers ton ChromeDriver
driver_path = r"chemin\vers\ton\dossier\chromedriver.exe"  # Mets ici le chemin vers chromedriver.exe

# Lancer le navigateur en mode headless
driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

# Ouvre la page Google
driver.get("https://www.google.com")

# (Optionnel) Imprimer le titre de la page pour confirmer
print("Titre de la page:", driver.title)

# Fermer le navigateur une fois la tâche terminée
driver.quit()
