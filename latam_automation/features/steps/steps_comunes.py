from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import locale
import time

@given('que abro el sitio de LATAM')
def step_open_latam(context):
    context.driver.get("https://latamairlines.com/co/es")
    WebDriverWait(context.driver, 15).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    time.sleep(2)  # Esperar carga

    # Intentar cerrar el modal si aparece
    try:
        close_btn = WebDriverWait(context.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "button-close-login-incentive"))
        )
        context.driver.execute_script("arguments[0].scrollIntoView(true);", close_btn)
        time.sleep(0.5)
        close_btn.click()
        print("✅ Modal de inicio de sesión cerrado.")
    except:
        print("⚠️ No apareció modal de inicio de sesión")


@when('selecciono opción \'Solo ida\'')
def step_solo_ida(context):
    try:
        print("🔍 Buscando botón 'Solo ida'...")
        solo_ida_btn = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-testid='fsb-one-way']"))
        )
        # Asegurarse de que esté visible en la pantalla
        context.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", solo_ida_btn)
        time.sleep(1)  # pequeña pausa para el efecto visual
        solo_ida_btn.click()
        print("✅ Botón 'Solo ida' clickeado correctamente.")
    except Exception as e:
        print(f"❌ Error al hacer clic en 'Solo ida': {e}")
        raise

@when('selecciono opción \'Ida y regreso\'')
def step_seleccionar_ida_y_vuelta(context):
    print("🔍 Buscando botón 'Ida y vuelta'...")
    try:
        ida_vuelta_btn = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='label' and text()='Ida y vuelta']"))
        )
        ida_vuelta_btn.click()
        print("✅ Botón 'Ida y vuelta' clickeado correctamente.")
        time.sleep(1)  # breve espera visual
    except TimeoutException:
        print("❌ No se encontró el botón 'Ida y vuelta'.")
        raise

@when('selecciono fecha de ida "{fecha_ida}"')
def step_seleccionar_fecha_ida(context, fecha_ida):
    print("📅 Seleccionando fecha de ida (solo ida)...")
    try:
        # Abrir el calendario
        calendario_ida = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="fsb-departure--text-field"]'))
        )
        calendario_ida.click()
        print("🟢 Calendario abierto (fecha ida - solo ida).")

        # Esperar a que aparezca la fecha deseada
        dia_element_ida = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f"[data-testid='date-{fecha_ida}']"))
        )
        context.driver.execute_script("arguments[0].click();", dia_element_ida)
        print(f"✅ Fecha de ida seleccionada: {fecha_ida}")

    except Exception as e:
        print(f"❌ Error al seleccionar la fecha de ida: {e}")
        raise e


@when('selecciono fechas de ida "{fecha_ida}" y regreso "{fecha_regreso}"')
def step_seleccionar_fechas_ida_regreso(context, fecha_ida, fecha_regreso):
    try:
        print("📅 Seleccionando fechas de ida y regreso...")

        # 1. Abrir calendario haciendo clic en el campo de fecha de ida
        campo_ida = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-testid="fsb-departure--text-field"]'))
        )
        campo_ida.click()
        print("🟢 Calendario abierto (fecha ida).")

        # 2. Seleccionar día de ida
        dia_element_ida = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f'span[id="date-{fecha_ida}"]'))
        )
        dia_element_ida.click()
        print(f"✅ Fecha de ida seleccionada: {fecha_ida}")

        time.sleep(1)  # Esperar que el calendario actualice

        # 3. Seleccionar día de regreso
        dia_element_regreso = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f'span[id="date-{fecha_regreso}"]'))
        )
        dia_element_regreso.click()
        print(f"✅ Fecha de regreso seleccionada: {fecha_regreso}")

    except TimeoutException:
        print("❌ No se pudieron seleccionar las fechas.")
        raise

@when('ingreso origen "{origen}"')
def step_ingresar_origen(context, origen):
    print("🔍 Buscando campo de origen (nuevo selector)...")

    campo_origen = WebDriverWait(context.driver, 15).until(
        EC.element_to_be_clickable((By.ID, "fsb-origin--text-field"))
    )
    campo_origen.clear()
    campo_origen.send_keys(origen)
    print(f"✍️ Ingresado origen: {origen}")

    # Esperar la sugerencia y seleccionarla
    sugerencia = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//ul[contains(@id,"autocomplete")]/li[1]'))
    )
    sugerencia.click()
    print("✅ Sugerencia de origen seleccionada.")


@when('ingreso destino "{destino}"')
def step_ingresar_destino(context, destino):
    print("🔍 Buscando campo de destino...")

    campo_destino = WebDriverWait(context.driver, 15).until(
        EC.element_to_be_clickable((By.ID, "fsb-destination--text-field"))
    )
    campo_destino.clear()
    campo_destino.send_keys(destino)
    print(f"✍️ Ingresado destino: {destino}")

    # Esperar la sugerencia y seleccionarla
    sugerencia = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//ul[contains(@id,"autocomplete")]/li[1]'))
    )
    sugerencia.click()
    print("✅ Sugerencia de destino seleccionada.")


@when('selecciono fechas de ida y regreso válidas')
def step_seleccionar_fechas(context):
    print("📅 Abriendo selector de fecha de ida...")

    try:
        # 1. Clic en el ícono del calendario
        fecha_icono = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="fsb-departure--text-field__end-icon-wrapper"]'))
        )
        fecha_icono.click()
        print("✅ Calendario abierto correctamente.")

        # 2. Esperar un momento para carga del calendario
        time.sleep(1)

        # 3. Clic en la fecha deseada directamente por data-testid
        print("🔍 Buscando fecha '16 julio 2025'...")
        fecha_deseada = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="date-2025-07-16"]'))
        )

        # Marcarla visualmente
        context.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", fecha_deseada)
        context.driver.execute_script("arguments[0].style.border='3px solid green';", fecha_deseada)

        # Clic
        fecha_deseada.click()
        print("✅ Fecha 16 de julio seleccionada correctamente.")
    
    except Exception as e:
        print(f"❌ Error seleccionando la fecha: {e}")
        raise e


@when('hago clic en buscar vuelo')
def step_click_buscar_vuelo(context):
    try:
        print("✈️ Buscando el botón 'Buscar vuelos'...")

        buscar_btn = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="fsb-search-flights--button"]'))
        )

        # Resaltar el botón visualmente
        context.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", buscar_btn)
        context.driver.execute_script("arguments[0].style.border='3px solid red';", buscar_btn)

        buscar_btn.click()
        print("✅ Botón 'Buscar vuelos' clickeado correctamente.")
    
    except Exception as e:
        print(f"❌ Error al hacer clic en 'Buscar vuelos': {e}")
        raise e


@then('deberían aparecer resultados de vuelo disponibles')
def step_ver_resultados(context):
    print("🕵️‍♂️ Esperando que redireccione a la página de resultados...")
    try:
        # Esperamos a que cambie la URL
        WebDriverWait(context.driver, 20).until(
            EC.url_contains("/ofertas-vuelos")
        )
        print("✅ URL de resultados detectada.")

        print("🔍 Esperando que aparezcan los resultados de vuelo (div con aria-label)...")
        WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@aria-label, 'Pesos colombianos')]")
            )
        )
        print("✅ Resultados de vuelo detectados correctamente.")
    except Exception as e:
        print("❌ No se encontraron los resultados de vuelos.")
        context.driver.save_screenshot("error_resultados.png")
        with open("html_resultados.html", "w", encoding="utf-8") as f:
            f.write(context.driver.page_source)
        raise e
    
@then("espero unos segundos")
def step_esperar(context):
    time.sleep(3)

