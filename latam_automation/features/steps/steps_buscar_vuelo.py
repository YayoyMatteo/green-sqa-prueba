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
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.maximize_window()
    context.driver.get("https://www.latamairlines.com/co/es")

    wait = WebDriverWait(context.driver, 10)
    try:
        aceptar_cookies = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
        aceptar_cookies.click()
    except:
        pass

@when('selecciono la opción de ida y regreso')
def step_tipo_viaje_ida_y_regreso(context):
    wait = WebDriverWait(context.driver, 10)
    try:
        ida_y_regreso_btn = wait.until(EC.element_to_be_clickable((By.ID, "roundtrip")))
        ida_y_regreso_btn.click()
    except Exception as e:
        print(f"❌ Error al seleccionar opción ida y regreso: {e}")

@when('ingreso origen "{origen}"')
def step_ingresar_origen(context, origen):
    wait = WebDriverWait(context.driver, 10)
    try:
        origen_input = wait.until(EC.element_to_be_clickable((By.ID, "searchbox-sbox-origin-input")))
        origen_input.click()
        origen_input.clear()
        origen_input.send_keys(origen)

        sugerencias = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.autocomplete__list li")))
        sugerencias[0].click()
    except Exception as e:
        print(f"❌ Error al ingresar origen: {e}")

@when('ingreso destino "{destino}"')
def step_ingresar_destino(context, destino):
    wait = WebDriverWait(context.driver, 10)
    try:
        destino_input = wait.until(EC.element_to_be_clickable((By.ID, "searchbox-sbox-destination-input")))
        destino_input.click()
        destino_input.clear()
        destino_input.send_keys(destino)

        sugerencias = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.autocomplete__list li")))
        sugerencias[0].click()
    except Exception as e:
        print(f"❌ Error al ingresar destino: {e}")

@when('selecciono una fecha de salida válida')
def step_seleccionar_fecha_ida(context):
    wait = WebDriverWait(context.driver, 10)
    try:
        fecha_ida = wait.until(EC.element_to_be_clickable((By.ID, "departure-date")))
        fecha_ida.click()
        dia_ida = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.date-picker__calendar-container button:not([disabled])")))
        dia_ida.click()
        print("✅ Fecha de salida seleccionada.")
    except Exception as e:
        print(f"❌ Error al seleccionar fecha de salida: {e}")

@when('selecciono fechas de ida y regreso válidas')
def step_seleccionar_fechas_ida_regreso(context):
    wait = WebDriverWait(context.driver, 10)
    try:
        fecha_ida = wait.until(EC.element_to_be_clickable((By.ID, "departure-date")))
        fecha_ida.click()

        dias = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.date-picker__calendar-container button:not([disabled])")))
        if len(dias) >= 2:
            dias[0].click()  # Fecha de ida
            WebDriverWait(context.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.date-picker__calendar-container button:not([disabled])")))
            dias = context.driver.find_elements(By.CSS_SELECTOR, "div.date-picker__calendar-container button:not([disabled])")
            if len(dias) >= 6:
                dias[5].click()  # Fecha de regreso
                print("✅ Fechas de ida y regreso seleccionadas.")
            else:
                print("⚠️ No se encontró una fecha de regreso adecuada.")
        else:
            print("⚠️ No se encontraron fechas suficientes.")
    except Exception as e:
        print(f"❌ Error al seleccionar fechas: {e}")

@when('hago clic en buscar vuelo')
def step_click_buscar(context):
    wait = WebDriverWait(context.driver, 10)
    try:
        buscar_btn = wait.until(EC.element_to_be_clickable((By.ID, "searchbox-sbox-button")))
        buscar_btn.click()
        print("✅ Se hizo clic en Buscar vuelo")
    except Exception as e:
        print(f"❌ Error al hacer clic en buscar vuelo: {e}")

@then('deberían aparecer resultados de vuelo disponibles')
def step_ver_resultados(context):
    wait = WebDriverWait(context.driver, 10)
    try:
        resultados = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[class*=itinerary-container]")))
        if resultados:
            print(f"✅ Se encontraron {len(resultados)} resultados de vuelo.")
        else:
            print("❌ No se encontraron resultados visibles.")
    except Exception as e:
        print(f"❌ Error al verificar resultados: {e}")
    finally:
        context.driver.quit()

@then('debería mostrar un mensaje de error')
def step_ver_mensaje_error(context):
    wait = WebDriverWait(context.driver, 10)
    try:
        mensaje_error = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".sbox-message__title, .error__title")))
        if mensaje_error:
            print("✅ Se mostró un mensaje de error.")
        else:
            print("❌ No se encontró mensaje de error visible.")
    except Exception as e:
        print(f"❌ Error al verificar mensaje de error: {e}")
    finally:
        context.driver.quit()
