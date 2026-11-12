p = "android/app/src/main/AndroidManifest.xml"
s = open(p, encoding="utf8").read()
if "mlkit.vision.DEPENDENCIES" not in s:
    s = s.replace("</application>", '    <meta-data android:name="com.google.mlkit.vision.DEPENDENCIES" android:value="barcode_ui"/>\n    </application>')
if "android.permission.CAMERA" not in s:
    s = s.replace("</manifest>", '    <uses-permission android:name="android.permission.CAMERA" />\n</manifest>')
open(p, "w", encoding="utf8").write(s)
print("Manifest listo")
