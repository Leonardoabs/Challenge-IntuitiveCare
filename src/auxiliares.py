from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def aguardar(driver, by, value, tempo=20):
    try:
        elemento = WebDriverWait(driver, tempo).until(
            EC.visibility_of_element_located((by, value))
        )
        return elemento
    except Exception:
        return None
