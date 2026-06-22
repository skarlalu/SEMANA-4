Estudiante: Karla Daniela Luque Navarrete
Este proyecto es una aplicación de consola en Python que simula la gestión básica de un restaurante aplicando los conceptos fundamentales de la Programación Orientada a Objetos y la organización modular.

La solución separa las responsabilidades dividiendo el sistema en modelos independientes, un servicio controlador y un script principal de ejecución.


El software está organizado bajo la siguiente estructura modular:

restaurante_app/
├── modelos/
│ ├── producto.py # Clase Producto (Atributos: nombre, precio)
│ └── cliente.py # Clase Cliente (Atributos: nombre, mesa)
├── servicios/
│ └── restaurante.py # Clase Restaurante (Gestión de colecciones y lógica)
└── main.py # Archivo principal que orquesta la ejecución del sistema

La organización modular del software mediante Programación Orientada a Objetos facilita un desarrollo más escalable, limpio y comprensible al fragmentar el sistema en responsabilidades independientes. Esta separación entre modelos de datos y servicios lógicos no solo simplifica la depuración de errores puntuales, sino que también optimiza la reutilización y el mantenimiento del código a largo plazo.
