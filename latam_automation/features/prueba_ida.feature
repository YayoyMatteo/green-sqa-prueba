Feature: Buscar vuelo solo ida

  Scenario: Buscar vuelo solo ida
    Given que abro el sitio de LATAM
    When selecciono la opción solo ida
    And ingreso origen "Bogotá"
    And ingreso destino "Medellín"
    And selecciono una fecha de salida válida
    And hago clic en buscar vuelo
    Then deberían aparecer resultados de vuelo disponibles
    Then espero unos segundos









