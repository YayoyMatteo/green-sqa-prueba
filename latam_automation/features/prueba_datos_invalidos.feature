Feature: Buscar vuelo con datos inválidos

  Scenario: Intentar buscar con datos inválidos
    Given que abro el sitio de LATAM
    When selecciono la opción solo ida
    And ingreso origen "XYZ"
    And ingreso destino "123"
    And hago clic en buscar vuelo
    Then debería mostrar un mensaje de error
    Then espero unos segundos

