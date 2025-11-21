"""Bu dosya, multimedya-guvenligi-ai projesindeki RBAC demo modülünü
kullanarak basit rol tabanlı erişim kontrolü örneği çalıştırır.
"""

from __future__ import annotations

import os
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PROJECT_ROOT = os.path.join(REPO_ROOT, "multimedya-guvenligi-ai")
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.access_control.rbac_demo import demo  # type: ignore[import]


if __name__ == "__main__":
    demo()
