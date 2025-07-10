Feature: Buscar vuelo ida y regreso

  Scenario: Buscar vuelo ida y regreso exitosamente
    Given que abro el sitio de LATAM
    When selecciono opción 'Ida y regreso'
    And ingreso origen "Bogotá"
    And ingreso destino "Buenos Aires"
    And selecciono fechas de ida "2025-07-16" y regreso "2025-07-24"
    And hago clic en buscar vuelo
    Then deberían aparecer resultados de vuelo disponibles
    And espero unos segundos
