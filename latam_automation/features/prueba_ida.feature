Feature: Buscar vuelo solo ida

  Scenario: Buscar vuelo solo ida exitosamente
    Given que abro el sitio de LATAM
    When selecciono opción 'Solo ida'
    And ingreso origen "Bogotá"
    And ingreso destino "Medellín"
    And selecciono fecha de ida "2025-07-16"
    And hago clic en buscar vuelo
    Then deberían aparecer resultados de vuelo disponibles
    And espero unos segundos








