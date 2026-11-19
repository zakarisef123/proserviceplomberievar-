# -*- coding: utf-8 -*-
"""Crée les variantes WebP des photos (src/assets/img/*.jpg -> src/assets/img/webp/<nom>-<largeur>.webp).

Usage : python3 src/make_webp.py   (nécessite Pillow : pip install pillow)
À relancer après l'ajout ou le remplacement d'une photo, puis `python3 src/build.py`.
Le build utilise automatiquement les variantes présentes (balise <picture> + srcset, JPEG de secours).
"""
import glob
import os

from PIL import Image

IMG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "img")
OUT = os.path.join(IMG, "webp")
WIDTHS = [480, 800, 1200]
HERO_WIDTHS = [640, 1024, 1440, 1920]  # photo de fond plein écran
QUALITY = 74
HERO_QUALITY = 55  # la photo de fond est couverte par un dégradé sombre


def main():
    os.makedirs(OUT, exist_ok=True)
    for old in glob.glob(os.path.join(OUT, "*.webp")):
        os.remove(old)
    for path in sorted(glob.glob(os.path.join(IMG, "*.jpg"))):
        name = os.path.splitext(os.path.basename(path))[0]
        im = Image.open(path).convert("RGB")
        widths = HERO_WIDTHS if name.startswith("hero") else WIDTHS
        sizes = sorted({min(w, im.width) for w in widths})
        for w in sizes:
            h = round(im.height * w / im.width)
            target = os.path.join(OUT, "%s-%d.webp" % (name, w))
            im.resize((w, h), Image.LANCZOS).save(target, "WEBP", quality=HERO_QUALITY if name.startswith("hero") else QUALITY, method=6)
            print("%-48s %6d o" % (os.path.relpath(target, IMG), os.path.getsize(target)))


if __name__ == "__main__":
    main()
