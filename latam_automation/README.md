# Automatización de Pruebas LATAM – GreenSQA

Yahir Garzón Mayorga



\# Automatización de Pruebas LATAM – GreenSQA



Este módulo automatiza el proceso de búsqueda de vuelos en el sitio web de LATAM utilizando Selenium + Behave (BDD).



---



\## Herramientas utilizadas



\- \*\*Selenium\*\*: Automatización del navegador

\- \*\*Behave\*\*: Framework BDD con Gherkin

\- \*\*Gherkin\*\*: Definición de escenarios

\- \*\*ChromeDriver\*\* + Google Chrome



---



\## Escenarios automatizados



1\. Vuelo de solo ida  

2\. Vuelo ida y regreso  

3\. Búsqueda con datos inválidos  



Cada escenario valida la apertura del sitio, ingreso de datos, fechas y resultados esperados.



---



\## Cómo ejecutar pruebas



Desde la raíz de la carpeta:



cd latam\_automation

python -m behave



# Estructura de modulo



latam\_automation/

├── features/

│   ├── buscar\_vuelo.feature

│   └── steps/

│       └── steps\_buscar\_vuelo.py

├── reportes/

├── requirements.txt

└── venv/ (opcional)



# Instalación de dependencias



pip install -r requirements.txt



# Recomendaciones



1. Asegúrese de tener Chrome instalado



2\. El archivo ChromeDriver debe ser compatible con la versión de navegador



3\. Ejecutar desde entorno virtual (venv: recomendado)

