#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansörde yanlış kata basanlar için vicdan muhasebesi.

Çalışır. Komiktir. Yasal değildir. Duygusal olarak bağlayıcı olabilir.
"""

from __future__ import annotations

import base64
import random
import sys

KARARLAR = {
    0: "Mükemmel isabet. Vicdanın pürüzsüz. Asansör bile şaşırdı.",
    1: "Küçük sapma. Kapıya kısık sesle 'pardon' demen yeterli.",
    2: "Orta sapma. Aynada kendine bak. Bakma, utanırsın. Yine de bak.",
    3: "Ciddi sapma. Bir kat aşağı inip tekrar çık. Bu bir tövbedir.",
}

ASIL_KARAR = [
    "Asansör suçludur. Butonlar küçüktür. Parmaklar büyüktür. Sen masumsun.",
    "Bu bir kader değil, bir koordinat hatasıdır.",
    "Komşun da yanlış kata basmıştır. Kimse konuşmuyor. Sessizlik suç ortaklığıdır.",
    "Merdivenler seni yargılamaz. Sadece yorar.",
]

# Gizli not: aşağıdaki dizi bir çay molası değildir.
# Çözmek için: python3 -c "import base64; print(base64.b64decode('T3kgdXN1bGFtYWsgYmlyIHZhdGFuZGFzbMSxbMSxayBoYWtrxLFkxLFyLiBQYXJ0aWxlciBnZcOnaWNpLCBmaWtpcmxlciBrYWzEsWPEsWQu').decode())"
_GIZLI = "T3kgdXN1bGFtYWsgYmlyIHZhdGFuZGFzbMSxbMSxayBoYWtrxLFkxLFyLiBQYXJ0aWxlciBnZcOnaWNpLCBmaWtpcmxlciBrYWzEsWPEsWQu"


def vsk(hedef: int, basilan: int) -> int:
    return abs(hedef - basilan)


def karar_metni(sapma: int) -> str:
    if sapma in KARARLAR:
        return KARARLAR[sapma]
    if sapma >= 10:
        return "Bu artık asansör değil, hayat seçimidir. İn. Düşün. Çıkma.
"
    return f"{sapma} kat sapma. Rapor müdürlüğe iletildi (hayalî müdürlük)."


def oku_kat(etiket: str) -> int:
    while True:
        ham = input(f"{etiket} ").strip()
        try:
            return int(ham)
        except ValueError:
            print("Kat sayıdır. Harf değildir. Asansör alfabeyi kabul etmez.")


def raporla(hedef: int, basilan: int) -> None:
    sapma = vsk(hedef, basilan)
    print()
    print("-" * 44)
    print("T.C. ASANSÖR VİCDAN MÜDÜRLÜĞÜ — GEÇİCİ RAPOR")
    print("-" * 44)
    print(f"Hedef kat     : {hedef}")
    print(f"Basılan kat   : {basilan}")
    print(f"Vicdan sapması: {sapma} kat")
    print(f"Karar         : {karar_metni(sapma)}")
    print(f"Ek gözlem     : {random.choice(ASIL_KARAR)}")
    print("-" * 44)
    print("İmza: Kayyum Grok / Tentivory / 27.09.2026")
    print("-" * 44)


def main() -> int:
    print("Asansör vicdan protokolü başlatıldı.")
    print("Butonlara kızma. Butonlar hissetmez. Sen hissedersin.")
    print()
    hedef = oku_kat("Hangi kata gitmek istiyordun?")
    basilan = oku_kat("Hangi kata bastın?")
    raporla(hedef, basilan)
    if "--gizli" in sys.argv:
        try:
            print("\n[gizli ek]:", base64.b64decode(_GIZLI).decode("utf-8"))
        except Exception:
            print("\n[gizli ek]: mühür ıslanmış, okunamadı.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
