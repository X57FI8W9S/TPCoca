# TP Coca-Cola – Correspondencia de Características

Integrantes:

Calabia, Juan Manuel
Cofré Villalón, Francisco

Detección de un logotipo de Coca-Cola en `tpcoca.ipynb`. Se generan descriptores usando SIFT y se "matchean" características con FLANN. Luego, se proyecta la ubicación del patrón sobre cada imagen objetivo.

Abrir `tpcoca.ipynb` y ejecutar las celdas en orden para generar los pares de descriptores, la homografía y visualizar los resultados sobre cada imagen de prueba. El script `template/crop_pattern.py` recorta el logo a partir de `template/pattern.png` para mejorar los resultados y `swap.ipynb` intercambia los colores del logo.

`multiples_detecciones.ipynb` Muestra la imagen con las detecciones y escribe total de logos detectados y tamaño del template usado.
