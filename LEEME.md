# Bodega de Obra: APK para Android

Aplicación de control de materiales (stock, facturas, entregas y pedido sugerido) con lector de códigos de barra por cámara.

## Cómo obtener el APK (sin instalar nada)

1. Cree una cuenta gratuita en github.com y un repositorio nuevo (privado o público).
2. Suba todo el contenido de esta carpeta al repositorio, incluida la carpeta oculta `.github`.
3. Entre a la pestaña **Actions**, elija **Compilar APK** y presione **Run workflow**.
4. Espere entre 5 y 10 minutos. Cuando termine, abra la ejecución y descargue **bodega-obra-apk** (viene dentro de un archivo .zip).
5. Pase `app-debug.apk` al teléfono y ábralo. Android pedirá permiso para instalar aplicaciones de este origen; acéptelo.

## Uso del lector

- Presione **Escanear código** en la pantalla principal, o **Escanear con la cámara** dentro de los formularios de material, entrega y factura.
- La primera vez, Android descarga el módulo del lector de Google. Toma unos segundos y requiere internet. Después funciona sin conexión.
- Asigne primero el código a cada material (Editar material, campo Código de barras). Así el lector lo encontrará después.

## Importante

- Los datos se guardan solo en el teléfono donde se instala la aplicación. No se comparten con otros teléfonos y se pierden si se desinstala.
- Es un APK de pruebas (debug). Sirve para instalar en sus equipos, pero no para publicarlo en Google Play.
