# TP Coca-Cola – Correspondencia de Características

Este repositorio contiene el material de un trabajo práctico orientado a la detección de un logotipo de Coca-Cola en distintas imágenes utilizando técnicas de visión por computadora. El cuaderno `tpcoca.ipynb` implementa un pipeline con SIFT para generar descriptores, FLANN para emparejar características y una homografía para proyectar la ubicación del patrón sobre cada imagen objetivo.

Abrir `tpcoca.ipynb` y ejecutar las celdas en orden para generar los emparejamientos, la homografía y visualizar los resultados sobre cada imagen de prueba. El script `template/crop_pattern.py` recorta la plantilla del logo a partir de `template/pattern.png` para mejorar los resultados y `swap.ipynb` intercambia los colores del logo.
