# TP Coca-Cola – Correspondencia de Características

Integrantes:

Calabia, Juan Manuel

Cofré Villalón, Francisco

### PUNTO 1

Detección de un logotipo de Coca-Cola en `PUNTO_1.ipynb`. Se generan descriptores usando SIFT y se "matchean" características con FLANN. Luego, se proyecta la ubicación del patrón sobre cada imagen objetivo.

Abrir `PUNTO_1.ipynb` y ejecutar las celdas en orden para generar los pares de descriptores, la homografía y visualizar los resultados sobre cada imagen de prueba. El script `template/crop_pattern.py` recorta el logo a partir de `template/pattern.png` para mejorar los resultados y `swap.ipynb` intercambia los colores del logo.

### PUNTO 2

`PUNTO_2.ipynb` muestra la imagen con las detecciones y escribe total de logos detectados y tamaño del template usado.

### PUNTO 3

`PUNTO_3.ipynb` generaliza el algoritmo del ítem 2 a las otras imágenes de `images/` y escribe los resultados en `resultados/`.
