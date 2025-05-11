# 📚🎬🎵 Administrador de Colección de Libros/Películas/Música

## Descripción del Proyecto

El **Administrador de Colección de Libros/Películas/Música** es una aplicación de consola desarrollada en Python que permite a los usuarios gestionar su colección personal de elementos culturales. Está diseñada para facilitar la organización de títulos, ya sean libros, películas o música, almacenando detalles como el autor, género y una valoración opcional.

El objetivo principal es ofrecer una herramienta simple pero eficaz para mantener un registro estructurado de la colección, acceder rápidamente a cualquier elemento y encontrar recomendaciones según criterios definidos.

---

## 🧩 Problemática

Muchas personas tienen dificultades para organizar y acceder a la información de sus colecciones personales cuando estas crecen. Esta aplicación soluciona problemas como:

- Desorden y falta de estructura en los registros.
- Dificultad para recordar detalles de cada elemento.
- Imposibilidad de realizar búsquedas rápidas por autor, título o género.

---

## ✅ Funcionalidades Principales

- **➕ Añadir Elemento:**  
  Permite registrar un nuevo libro, película o canción especificando:
  - Título  
  - Autor/Director/Artista  
  - Género  
  - Valoración (opcional)  
  Los datos se guardan automáticamente en un archivo JSON.

- **📋 Listar Elementos:**  
  Muestra todos los elementos registrados, con opción de filtrar por:
  - Categoría (libro, película o música)
  - Género

- **🔍 Buscar Elemento:**  
  Búsqueda por título, autor o género para encontrar información específica de manera rápida.

- **✏️ Editar Elemento:**  
  Modifica los datos de un elemento específico, como el título o valoración, y actualiza el archivo JSON.

- **❌ Eliminar Elemento:**  
  Elimina un elemento por su título o identificador para mantener la colección actualizada.

- **💾 Guardar y Cargar desde JSON:**  
  - Al iniciar, carga automáticamente la colección desde un archivo JSON.  
  - Al cerrar, guarda todos los cambios realizados.

---

## 🛠️ Requisitos y Tecnologías

### Requisitos del Sistema
- Python 3.13
- Librerías externas:
  - `tabulate` (para mostrar tablas en consola)

```bash
pip install tabulate
