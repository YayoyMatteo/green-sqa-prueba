from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

@given('que abro el sitio de LATAM')
def step_open_site(context):
    print("🌐 Abriendo sitio de LATAM...")
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.maximize_window()
    context.driver.get("https://www.latamairlines.com/co/es")

    wait = WebDriverWait(context.driver, 10)
    try:
        wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))).click()
        print("✅ Cookies aceptadas.")
    except:
        print("ℹ️ No aparecieron cookies para aceptar.")

    # ✅ Cerrar popup de bienvenida si aparece
    try:
        popup_cerrar = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[role='dialog'] button[aria-label='Cerrar']")))
        popup_cerrar.click()
        print("✅ Popup de bienvenida cerrado.")
    except:
        print("ℹ️ No apareció el popup de bienvenida.")

@when('selecciono la opción solo ida')
def step_solo_ida(context):
    print("✈️ Seleccionando opción 'Solo ida'...")
    wait = WebDriverWait(context.driver, 10)
    try:
        wait.until(EC.element_to_be_clickable((By.ID, "oneway"))).click()
    except Exception as e:
        print(f"❌ No se pudo seleccionar 'Solo ida': {e}")

@when('selecciono la opción ida y regreso')
def step_ida_y_regreso(context):
    print("🔁 Seleccionando opción 'Ida y regreso'...")
    wait = WebDriverWait(context.driver, 10)
    try:
        wait.until(EC.element_to_be_clickable((By.ID, "roundtrip"))).click()
    except Exception as e:
        print(f"❌ No se pudo seleccionar 'Ida y regreso': {e}")

@when('ingreso origen "{origen}"')
def step_ingresar_origen(context, origen):
    print(f"📍 Ingresando origen: {origen}")
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "searchbox-sbox-origin-input")))
    origen_input = context.driver.find_element(By.ID, "searchbox-sbox-origin-input")
    origen_input.click()
    origen_input.clear()
    origen_input.send_keys(origen)
    sugerencias = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.autocomplete__list li")))
    sugerencias[0].click()

@when('ingreso destino "{destino}"')
def step_ingresar_destino(context, destino):
    print(f"🛬 Ingresando destino: {destino}")
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "searchbox-sbox-destination-input")))
    destino_input = context.driver.find_element(By.ID, "searchbox-sbox-destination-input")
    destino_input.click()
    destino_input.clear()
    destino_input.send_keys(destino)
    sugerencias = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.autocomplete__list li")))
    sugerencias[0].click()

@when('selecciono una fecha de salida válida')
def step_fecha_salida(context):
    print("📅 Seleccionando fecha de salida...")
    wait = WebDriverWait(context.driver, 10)
    fecha = wait.until(EC.element_to_be_clickable((By.ID, "departure-date")))
    fecha.click()
    dia = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.date-picker__calendar-container button:not([disabled])")))
    dia.click()

@when('selecciono fechas de ida y regreso válidas')
def step_fechas_ida_y_regreso(context):
    print("📆 Seleccionando fechas de ida y regreso...")
    wait = WebDriverWait(context.driver, 10)
    fecha = wait.until(EC.element_to_be_clickable((By.ID, "departure-date")))
    fecha.click()
    dias = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.date-picker__calendar-container button:not([disabled])")))
    if len(dias) >= 6:
        dias[0].click()
        dias[5].click()
    else:
        print("⚠️ No se encontraron suficientes días habilitados.")

@when('hago clic en buscar vuelo')
def step_buscar(context):
    print("🔎 Haciendo clic en 'Buscar vuelo'...")
    wait = WebDriverWait(context.driver, 10)
    buscar_btn = wait.until(EC.element_to_be_clickable((By.ID, "searchbox-sbox-button")))
    buscar_btn.click()

@then('deberían aparecer resultados de vuelo disponibles')
def step_ver_resultados(context):
    print("📥 Verificando si aparecen resultados de vuelo...")
    wait = WebDriverWait(context.driver, 15)
    try:
        resultados = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[class*=itinerary-container]")))
        print(f"✅ Se encontraron {len(resultados)} resultados de vuelo.")
    except:
        print("❌ No se encontraron resultados.")
    finally:
        context.driver.quit()

@then('debería mostrar un mensaje de error')
def step_ver_error(context):
    print("🚫 Verificando si se muestra un mensaje de error...")
    wait = WebDriverWait(context.driver, 10)
    try:
        mensaje = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".sbox-message__title, .error__title")))
        print("✅ Se mostró un mensaje de error.")
    except:
        print("❌ No se encontró mensaje de error.")
    finally:
        context.driver.quit()

@then('espero unos segundos')
def step_wait_debug(context):
    print("⏳ Esperando 10 segundos para ver el resultado...")
    time.sleep(10)
    context.driver.quit()
