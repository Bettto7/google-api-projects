# Proyecto de conexión a Google Analytics 4 (GA4)

Este proyecto conecta a una propiedad de GA4 usando la API oficial `analyticsdata` (v1beta) y una cuenta de servicio.

## Instrucciones

1. Instala las dependencias:
```
pip install -r requirements.txt
```

2. Coloca tu archivo `cuenta-servicio-ga.json` en la raíz del proyecto.

3. Reemplaza `TU_ID_PROPIEDAD` en `ga4_consulta.py` con tu ID real de propiedad GA4.

4. Comparte acceso a la propiedad con el correo de la cuenta de servicio desde Google Analytics (rol: Lector).

5. Ejecuta el script:
```
python ga4_consulta.py
```
