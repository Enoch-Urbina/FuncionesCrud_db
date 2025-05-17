-Paso_1: Crear la base de datos con el script proporcionado. 
    mysql -u tu_usuario -p nombre_de_base_datos < "C:\Users\1103670981\Desktop\CuartoSemestre\TopicosS4A\Tema-4\db23270637.sql"

-Paso_2: Abrir el proyecto en Visual Studio Code

-Paso_3: Crear el entorno virtual con el siguiente comando:
    python -m venv env23270637

-paso_4: Activar el entorno virtual.
    * En Windows: env23270637\Scripts\activate
    * En Linux/Mac: source env23270637/bin/activate

-Paso_5: Instalar las librerías necesarias para el funcionamiento del código.
    Comandos a ejecutar:
    pip install pyqt6
    pip install mysql-connector-python

-Paso_6: Configurar el código del archivo conexiondb.py con los datos de su gestor de base de datos.

-Paso_7: Crear el archivo .gitignore para excluir el entorno virtual env23270637

-Paso_8: Ejecutar cada archivo con su nombre en la terminal, ejemplo:
    interfaz_cliente.py

