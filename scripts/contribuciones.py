# Mete la serpiente dentro de la tarjeta "Mis contribuciones"
import re
import sys

serpiente, marco, salida = sys.argv[1:4]

svg = open(serpiente, encoding="utf-8").read()
svg = re.sub(r'<svg ([^>]*?)width="[\d.]+" height="[\d.]+"',
             r'<svg x="20" y="92" width="820" height="179" \1', svg, count=1)

tarjeta = open(marco, encoding="utf-8").read()
open(salida, "w", encoding="utf-8").write(tarjeta.replace("<!--SERPIENTE-->", svg))
