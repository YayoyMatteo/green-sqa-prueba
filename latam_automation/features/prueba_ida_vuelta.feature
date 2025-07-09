Feature: Buscar vuelo ida y regreso

  Scenario: Buscar vuelo ida y regreso
    Given que abro el sitio de LATAM
    When selecciono la opción ida y regreso
    And ingreso origen "Bogotá"
    And ingreso destino "Buenos Aires"
    And selecciono fechas de ida y regreso válidas
    And hago clic en buscar vuelo
    Then deberían aparecer resultados de vuelo disponibles
    Then espero unos segundos

