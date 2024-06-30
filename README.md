# UrbanRoutes

En este proyecto, se quiere automatizar (E2E) el proceso para solicitar el servicio de reserva de taxi, partiendo de una dirección A con destino a una dirección B, así como tambien se automatizan los servicios adicionales al medio de transporte, como puede ser un requisito para el conductor, o simplemente un pedido que incluya una orden de helado.

Es importante mencionar que la prueba automatizada va a tener en cuenta los siguientes requerimientos:
 ```
Dirección de Origen: 'East 2nd Street, 601'
Dirección de Destino: '1300 1st St'
Número de Telefono = '+1 123 123 12 12'
Número de Tarjeta, Codigo de tarjeta = '1234 5678 9100', '111'
Pedido especial para el conductor = 'trae 2 botellas de agua'
 ```

# POM

El Modelo de Objetos de Página (POM, por sus siglas en inglés) es un patrón de diseño utilizado en pruebas automatizadas de interfaces de usuario (UI). Este patrón ayuda a crear una estructura más mantenible y legible al separar la lógica de la UI del código de las pruebas.

Descripción del Modelo de Objetos de Página (POM)
1. Separación de Concerns:

Página de Objetos: Cada página de la aplicación se modela como una clase independiente. Esta clase contiene todos los elementos de la página y las acciones que se pueden realizar en ellos.
Clases de Prueba: Las pruebas se centran en la lógica de verificación y utilizan las clases de página para interactuar con la UI.
2. Mejora de la Mantenibilidad:

Cuando los elementos de la UI cambian, solo se necesita actualizar el código en la clase de la página correspondiente, no en todas las pruebas que interactúan con esos elementos.
3. Reutilización de Código:

Las acciones comunes se pueden reutilizar en múltiples pruebas, lo que reduce la duplicación de código y facilita la creación de pruebas complejas.
4. Mayor Legibilidad:

Las clases de prueba son más legibles ya que se centran en las acciones y verificaciones en lugar de en los detalles de la implementación de la UI.

# Guía de Instalación Rápida

## Requisitos Previos

- Sistema Operativo: Windows, macOS, o Linux
- Editor: PyCharm (Community o Professional)

## Paso 1: Instalar Python 3

1. **Descargar Python:**
   - Visita [python.org](https://www.python.org/downloads/) y descarga la última versión de Python 3 para tu sistema operativo.

2. **Instalar Python:**
   - Ejecuta el instalador y asegúrate de seleccionar la opción "Add Python to PATH" antes de continuar con la instalación.

## Paso 2: Instalar PyCharm

1. **Descargar PyCharm:**
   - Visita [jetbrains.com/pycharm/download](https://www.jetbrains.com/pycharm/download/) y descarga la versión Community (gratuita) o Professional.

2. **Instalar PyCharm:**
   - Ejecuta el instalador y sigue las instrucciones en pantalla para completar la instalación.

## Paso 3: Crear un Nuevo Proyecto en PyCharm

1. **Abrir PyCharm:**
   - Abre PyCharm y selecciona `File` > `New Project`.

2. **Configurar el Proyecto:**
   - Elige una ubicación para tu nuevo proyecto.
   - Selecciona la versión de Python 3 que instalaste anteriormente como el intérprete del proyecto.

## Paso 4: Instalar Pip

1. **Verificar pip:**
   - Pip se instala automáticamente con Python 3. Puedes verificar la instalación abriendo el terminal en PyCharm (`View` > `Tool Windows` > `Terminal`) y ejecutando:
     ```sh
     pip --version
     ```

## Paso 5: Instalar Selenium, WebDriver Manager y Pytest

1. **Abrir el Terminal en PyCharm:**
   - Ve a `View` > `Tool Windows` > `Terminal`.

2. **Instalar Selenium y WebDriver Manager:**
   - Ejecuta los siguientes comandos en el terminal:
     ```sh
     pip install selenium
     pip install webdriver-manager
     ```

3. **Instalar pytest:**
   - Ejecuta el siguiente comando en el terminal:
     ```sh
     pip install pytest
     ```

## Paso 6: Configurar WebDriver

1. **Añadir Código de Ejemplo:**
   - Crea un archivo Python (por ejemplo, `test_example.py`) y añade el siguiente código para verificar que todo está configurado correctamente:

     ```python
     from selenium import webdriver
     from selenium.webdriver.common.by import By
     from webdriver_manager.chrome import ChromeDriverManager
     import pytest

     @pytest.fixture
     def setup():
         driver = webdriver.Chrome(ChromeDriverManager().install())
         driver.implicitly_wait(10)
         yield driver
         driver.quit()

     def test_google_search(setup):
         driver = setup
         driver.get("https://www.google.com")
         assert "Google" in driver.title
     ```

2. **Ejecutar la Prueba:**
   - Ejecuta el script desde el terminal usando pytest:
     ```sh
     pytest test_example.py
     ```

## Resumen de Comandos

```sh
# Verificar la instalación de pip
pip --version

# Instalar Selenium y WebDriver Manager
pip install selenium
pip install webdriver-manager

# Instalar pytest
pip install pytest

# Ejecutar las pruebas con pytest
pytest test_example.py
```

# Como iniciar las pruebas...

Una vez tengas instalado Python, Pytest y Pycharm, vas a poder editar el codigo y ejecutar las pruebas que consideres necesarias ejecutando el archivo main.py.

En el archivo UrbanRoutesPage.py vas a encontrar los metodos, que utilizan los localizadores que se encuentran en el archivo Locators.py. Las pruebas están en la clase TestUrbanRoutes en el archivo Main.py.



## Contribuciones

Haz la diferencia en el mundo del software contribuyendo a nuestro proyecto de automatización de pruebas de código abierto. ¡Tu aporte es valioso! 

Contribuciones son siempre bienvenidas.

## License

MIT

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)
