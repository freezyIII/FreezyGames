from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Configuration du mode headless pour ne pas afficher la fenêtre
options = Options()
options.headless = True  # C'est ce qui fait que la fenêtre du navigateur est invisible

# Initialiser le navigateur
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# Ouvrir la page Google
driver.get("https://www.google.com")

# Effectuer des actions si nécessaire, par exemple rechercher quelque chose :
# search_box = driver.find_element("name", "q")
# search_box.send_keys("Python")
# search_box.submit()

# Attends un peu pour simuler des actions (tu peux ajuster selon ton besoin)
driver.quit()
