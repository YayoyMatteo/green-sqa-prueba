Feature: Prueba de apertura

Scenario: Buscar vuelo con datos inválidos
  Given que abro el sitio de LATAM
  When ingreso origen "XYZ"
  And ingreso destino "123"
  And hago clic en buscar vuelo
  Then debería mostrar un mensaje de error






