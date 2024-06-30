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

## Installation

1. Ensuring PyCharm is Installed

Download and install the latest version of PyCharm from the JetBrains website: https://www.jetbrains.com/pycharm/download/
2. Creating a Virtual Environment (Recommended)

In PyCharm, open your project or create a new one.
Go to ```File``` -> ```Settings (or PyCharm``` -> ```Preferences``` on macOS).
Navigate to ```Project: <your project name> ```-> ```Python Interpreter.```
Click the gear icon next to the interpreter dropdown and choose "Add Interpreter".
Select "Virtualenv Environment".
Choose a base interpreter (usually the latest Python version available) and specify a location for the virtual environment.
Check the "Inherit global site-packages" box if you want to use existing packages.
Click "OK" to create the virtual environment.

3. Installing Pip (Usually Pre-Installed)

Pip is the package installer for Python and typically comes pre-installed with Python.

To check if Pip is installed, open PyCharm's terminal and run:
```
Bash
pip --version
```

content_copy
If you get a version number, Pip is installed. Otherwise, follow the instructions for your operating system on the official Pip website: https://pip.pypa.io/en/stable/installation/

4. Installing Pytest and Selenium

Pytest:

Open the PyCharm terminal.

Run the following command:

```
pip install pytest
```

Selenium:

Open the PyCharm terminal.

Run the following command:

```sh
pip install selenium
```

PyCharm will automatically download and install the packages.


5. Verification

You can verify that Pytest and Selenium are installed by trying to import them in your Python code:

Python
```import pytest
from selenium import webdriver
```

If there are no errors, the installation was successful.
Alternative Installation Method (Using PyCharm's GUI)

Go to File -> Settings (or PyCharm -> Preferences on macOS).
Navigate to Project: <your project name> -> Python Interpreter.
Click the "+" button to open the "Available Packages" window.
Search for "pytest" and "selenium".
Click "Install Package" for each of them.

Additional Tips

WebDrivers: Selenium requires a browser driver to interact with the browser. Download the appropriate driver (e.g., ChromeDriver for Chrome) and make sure it's in your system's PATH or provide its location explicitly in your code.

Project Structure: Organize your PyCharm project with separate directories for tests, page objects, and other components.

Updates: Keep your packages up-to-date with the following command:

Bash
```
pip install --upgrade pytest selenium
```
# Como iniciar las pruebas...

Una vez tengas instalado Python, Pytest y Pycharm, vas a poder editar el codigo y ejecutar las pruebas que consideres necesarias ejecutando el archivo main.py.

En el archivo main.py vas a encontrar los localizadores y metodos están en la clase UrbanRoutesPage. Las pruebas están en la clase TestUrbanRoutes



## Contribuciones

Haz la diferencia en el mundo del software contribuyendo a nuestro proyecto de automatización de pruebas de código abierto. ¡Tu aporte es valioso! 

Contribuciones son siempre bienvenidas.

## License

MIT

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)
