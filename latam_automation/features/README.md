# Prueba Técnica - GreenSQA 

Este repositorio contiene un proyecto de automatización de pruebas funcionales para el sitio web de LATAM Airlines, usando `Behave` y `Selenium`.

## Estructura del Proyecto

```
latam-automation/
├── features/
│   ├── prueba_ida.feature
│   ├── prueba_ida_vuelta.feature
│   ├── steps/
│   │   └── steps_comunes.py
│   └── environment.py
├── drivers/
│   └── [WebDriver correspondiente]
├── requirements.txt
└── README.md
```

## Requisitos

- Python 3.10 o superior
- Google Chrome instalado
- ChromeDriver correspondiente en la carpeta `drivers/`

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/YayoyMatteo/green-sqa-prueba.git
cd green-sqa-prueba/latam-automation
```

2. Crea un entorno virtual (opcional pero recomendado):

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución de Pruebas

### 1. Búsqueda de vuelo solo ida:

```bash
python -m behave features/prueba_ida.feature
```

### 2. Búsqueda de vuelo ida y vuelta:

```bash
python -m behave features/prueba_ida_vuelta.feature
```

## Autor

- 👤 [Yayoy Matteo](https://github.com/YayoyMatteo)

## Licencia

Este proyecto es solo para fines de demostración técnica.