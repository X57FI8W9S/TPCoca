# TP Coca-Cola – Correspondencia de Características

Detección de un logotipo de Coca-Cola en `tpcoca.ipynb`. Se generan descriptores usando SIFT y se "matchean" características con FLANN. Luego, se proyecta la ubicación del patrón sobre cada imagen objetivo.

Abrir `tpcoca.ipynb` y ejecutar las celdas en orden para generar los emparejamientos, la homografía y visualizar los resultados sobre cada imagen de prueba. El script `template/crop_pattern.py` recorta el logo a partir de `template/pattern.png` para mejorar los resultados y `swap.ipynb` intercambia los colores del logo.
