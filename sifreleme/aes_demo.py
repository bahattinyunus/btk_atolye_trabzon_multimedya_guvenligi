"""Bu dosya, multimedya-guvenligi-ai projesindeki AES-benzeri
symmetric_aes_demo modülünü kullanarak basit bir şifreleme/çözme
örneği çalıştırır.

Klasör yapısı gereği, bu scriptin doğru çalışması için
`multimedya-guvenligi-ai` projesi aynı repo kökünde bulunmalıdır.
"""

from __future__ import annotations

import os
import sys

# Repo kökü: sifreleme klasöründen bir üst dizin
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PROJECT_ROOT = os.path.join(REPO_ROOT, "multimedya-guvenligi-ai")
SRC_ROOT = os.path.join(PROJECT_ROOT, "src")

if SRC_ROOT not in sys.path:
    sys.path.insert(0, SRC_ROOT)

from crypto.symmetric_aes_demo import demo  # type: ignore[import]


if __name__ == "__main__":
    demo()
