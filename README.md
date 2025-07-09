# 🧠 Red Neuronal - Conversión de Km a Millas (con PyTorch)

Este proyecto utiliza **PyTorch** para entrenar una red neuronal que convierte kilómetros a millas. Está desarrollado con principios de programación orientada a objetos (POO) y estructura modular siguiendo buenas prácticas.
Por que pytorch? Por que al tener la version 3.13.5 de python aún no es compatible con TensorFlow

## 🚀 Requisitos

- Python 3.13 (o compatible)
- pip
- torch, numpy, matplotlib

---

## 🛠 Instalación y uso

### 1. Clonar o descargar el proyecto

Si descargaste el `.zip`, descomprimilo y entrá a la carpeta:

```bash
cd convertidor_km_millas_pytorch
```

### 2. Crear entorno virtual (opcional pero recomendado)

#### En Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### En Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar el programa

```bash
python main.py
```

---

## 🧪 ¿Qué hace el programa?

1. Entrena una red neuronal para aprender la conversión de kilómetros a millas.
2. Muestra una gráfica del entrenamiento (curva de pérdida).
3. Luego, te permite probar valores manualmente desde consola.

📌 Ejemplo:

```
🚗 Conversor de kilómetros a millas (usando red neuronal)

Ingresá una cantidad de kilómetros (o escribí 'salir' para terminar): 10
10 km son aproximadamente 6.213 millas.
```

---

## 📁 Estructura del proyecto

```
convertidor_km_millas_pytorch/
│
├── main.py                   # Punto de entrada
├── requirements.txt          # Dependencias
├── README.md                 # Documentación
│
├── data/
│   └── dataset.py            # Datos de entrenamiento
│
├── model/
│   └── modelo.py             # Red neuronal (PyTorch)
│
├── services/
│   └── predictor.py          # Lógica de predicción
│
└── utils/
    └── visualizer.py         # Visualización del entrenamiento
```

---

## 🤖 Librerías utilizadas

- [PyTorch](https://pytorch.org/)
- NumPy
- Matplotlib

---
