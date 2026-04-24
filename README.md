# Actividad 8 - Integración Continua

## 📌 Descripción del Proyecto

Este proyecto implementa un módulo en Python basado en la aplicación Backhaul, el cual permite calcular la prioridad de cargas para transportistas en función de distintos criterios como urgencia, distancia, espacio disponible y reputación.

El objetivo principal es aplicar conceptos de Gestión de la Configuración e Integración Continua mediante la automatización de pruebas y validaciones del código.

---

## 🚀 Instrucciones para clonar y ejecutar el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/Alescallier/actividad-8-ci-python-ing-soft-3.git
cd actividad-8-ci-python-ing-soft-3
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Ejecutar pruebas

```bash
pytest
```

---

## ⚙️ Integración Continua (CI)

Se implementó un pipeline de Integración Continua utilizando **GitHub Actions**, el cual se ejecuta automáticamente ante cada cambio en el repositorio (push o pull request).

### 🔗 Archivo de configuración del CI

El pipeline se encuentra definido en el siguiente archivo:

👉 `.github/workflows/ci.yml`

---

## 🔄 Funcionamiento del pipeline

El pipeline realiza automáticamente las siguientes tareas:

1. Clona el repositorio
2. Configura el entorno de Python
3. Instala las dependencias del proyecto
4. Ejecuta pruebas unitarias con **pytest**
5. Verifica el estilo del código con **flake8**

Si alguna de estas etapas falla, el pipeline se detiene e impide la integración del código a la rama principal. Esto garantiza que solo código validado y sin errores sea incorporado al proyecto.

---

## 🧪 Validación del sistema

Durante el desarrollo se simularon distintos errores para comprobar el funcionamiento del pipeline:

* Error en pruebas unitarias (lógica incorrecta)
* Error de estilo detectado por el linter

En ambos casos, el pipeline detectó los errores correctamente y evitó su integración hasta ser corregidos.

---

## 📁 Tecnologías utilizadas

* Python
* pytest
* flake8
* GitHub Actions

---

## 👨‍💻 Autores

Escallier Alejandro, Meyer Ivan, Monzon Sebastian, Rojas Carlos Victor, Barreyro Luciano
