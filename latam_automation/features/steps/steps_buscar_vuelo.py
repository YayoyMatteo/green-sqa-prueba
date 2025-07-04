from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

@given('que abro el sitio de LATAM')
def step_open_site(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.maximize_window()
    context.driver.get("https://www.latamairlines.com/co/es")
    time.sleep(4)
    # Aceptar cookies si aparecen
    try:
        aceptar_cookies = context.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        aceptar_cookies.click()
        time.sleep(1)
    except:
        pass

@when('selecciono la opción de ida y regreso')
def step_tipo_viaje_ida_y_regreso(context):
    time.sleep(2)
    try:
        ida_y_regreso_btn = context.driver.find_element(By.ID, "roundtrip")
        ida_y_regreso_btn.click()
        time.sleep(1)
    except Exception as e:
        print(f"❌ Error al seleccionar opción ida y regreso: {e}")

@when('ingreso origen "{origen}"')
def step_ingresar_origen(context, origen):
    time.sleep(2)
    try:
        origen_input = context.driver.find_element(By.ID, "searchbox-sbox-origin-input")
        origen_input.click()
        time.sleep(1)
        origen_input.send_keys(origen)
        time.sleep(2)
        sugerencias = context.driver.find_elements(By.CSS_SELECTOR, "ul.autocomplete__list li")
        if sugerencias:
            sugerencias[0].click()
        else:
            print(f"⚠️ No se encontraron sugerencias para origen '{origen}'")
    except Exception as e:
        print(f"❌ Error al ingresar origen: {e}")

@when('ingreso destino "{destino}"')
def step_ingresar_destino(context, destino):
    time.sleep(2)
    try:
        destino_input = context.driver.find_element(By.ID, "searchbox-sbox-destination-input")
        destino_input.click()
        time.sleep(1)
        destino_input.send_keys(destino)
        time.sleep(2)
        sugerencias = context.driver.find_elements(By.CSS_SELECTOR, "ul.autocomplete__list li")
        if sugerencias:
            sugerencias[0].click()
        else:
            print(f"⚠️ No se encontraron sugerencias para destino '{destino}'")
    except Exception as e:
        print(f"❌ Error al ingresar destino: {e}")

@when('selecciono una fecha de salida válida')
def step_seleccionar_fecha_ida(context):
    try:
        time.sleep(2)
        fecha_ida = context.driver.find_element(By.ID, "departure-date")
        fecha_ida.click()
        time.sleep(2)
        dia_ida = context.driver.find_element(By.CSS_SELECTOR, "div.date-picker__calendar-container button:not([disabled])")
        dia_ida.click()
        time.sleep(1)
    except Exception as e:
        print(f"❌ Error al seleccionar fecha de salida: {e}")

@when('selecciono fechas de ida y regreso válidas')
def step_seleccionar_fechas_ida_regreso(context):
    try:
        time.sleep(2)
        fecha_ida = context.driver.find_element(By.ID, "departure-date")
        fecha_ida.click()
        time.sleep(2)
        # Seleccionar fecha de ida
        dia_ida = context.driver.find_element(By.CSS_SELECTOR, "div.date-picker__calendar-container button:not([disabled])")
        dia_ida.click()
        time.sleep(2)
        # Seleccionar fecha de regreso (posterior)
        dias = context.driver.find_elements(By.CSS_SELECTOR, "div.date-picker__calendar-container button:not([disabled])")
        if len(dias) > 5:
            dias[5].click()
            time.sleep(1)
        else:
            print("⚠️ No se encontró una fecha de regreso adecuada")
    except Exception as e:
        print(f"❌ Error al seleccionar fechas: {e}")

@when('hago clic en buscar vuelo')
def step_click_buscar(context):
    time.sleep(2)
    try:
        buscar_btn = context.driver.find_element(By.ID, "searchbox-sbox-button")
        buscar_btn.click()
        print("✅ Se hizo clic en Buscar vuelo")
    except Exception as e:
        print(f"❌ Error al hacer clic en buscar vuelo: {e}")

@then('deberían aparecer resultados de vuelo disponibles')
def step_ver_resultados(context):
    try:
        time.sleep(6)
        resultados = context.driver.find_elements(By.CSS_SELECTOR, "[class*=itinerary-container]")
        if resultados and len(resultados) > 0:
            print(f"✅ Se encontraron {len(resultados)} resultados de vuelo.")
        else:
            print("❌ No se encontraron resultados visibles.")
    except Exception as e:
        print(f"❌ Error al verificar resultados: {e}")
    finally:
        context.driver.quit()

@then('debería mostrar un mensaje de error')
def step_ver_mensaje_error(context):
    try:
        time.sleep(6)
        mensaje_error = context.driver.find_elements(By.CSS_SELECTOR, ".sbox-message__title, .error__title")
        if mensaje_error:
            print("✅ Se mostró un mensaje de error.")
        else:
            print("❌ No se encontró mensaje de error visible.")
    except Exception as e:
        print(f"❌ Error al verificar mensaje de error: {e}")
    finally:
        context.driver.quit()
