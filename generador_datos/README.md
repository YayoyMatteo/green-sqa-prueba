# Generador de Datos – GreenSQA

Yahir Garzón Mayorga



\#Generador de Datos – GreenSQA



Este módulo genera datos falsos de personas y empresas utilizando la librería `Faker`. Los datos se guardan en un archivo `.csv` y en una base de datos `SQLite`.



---



\##Funcionalidades



\- Generación de usuarios con nombre, documento, correo, empresa, etc.

\- Almacenamiento en `datos\_generados.csv`

\- Almacenamiento en `datos\_generados.db` (SQLite)

\- Interfaz por consola para:

&nbsp; - Generar nuevos registros

&nbsp; - Visualizar los registros existentes





\##Cómo ejecutar



Desde la terminal:



cd generador\_datos

python main.py



# Estructura del modulo



generador\_datos/

├── main.py

├── models/

│   ├── base\_user.py

│   ├── company.py

│   └── person.py

├── services/

│   ├── data\_generator.py

│   └── csv\_exporter.py

├── utils/

├── datos\_generados.csv

├── datos\_generados.db

└── requirements.txt



# Requisitos



pip install -r requirements.txt



# Librerías usadas



faker

sqlite3 (estándar de Python)







