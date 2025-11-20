"""Basit bir ABAC (Attribute-Based Access Control) demo modülü.

Kullanıcı, kaynak ve ortam attribute'larına göre politika kararı verir.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass
class Subject:
    username: str
    department: str
    location: str


@dataclass
class Resource:
    name: str
    classification: str  # public / internal / confidential


@dataclass
class Environment:
    hour: int  # 0-23


def policy_allow(subject: Subject, resource: Resource, env: Environment, action: str) -> bool:
    """Örnek ABAC politikası.

    Kurallar:
      - 'confidential' kaynaklara sadece 'IT' departmanı erişebilir.
      - Mesai dışı saatlerde (>= 19) yazma izni yoktur.
      - 'public' kaynaklara herkes okuyabilir.
    """

    if resource.classification == "public" and action == "read":
        return True

    if resource.classification == "confidential" and subject.department != "IT":
        return False

    if action in {"write", "delete"} and env.hour >= 19:
        return False

    # Varsayılan basit kural: internal/confidential için IT departmanı okuyabilir/yazabilir.
    if subject.department == "IT":
        return True

    return False


def demo() -> None:
    """ABAC karar mekanizmasını gösteren basit bir demo.

    Çalıştırmak için:
        python -m src.access_control.abac_demo
    """

    subject = Subject(username="ali", department="HR", location="office")
    admin = Subject(username="ayse", department="IT", location="office")

    public_doc = Resource(name="duyuru.pdf", classification="public")
    secret_doc = Resource(name="butce.xlsx", classification="confidential")

    day_env = Environment(hour=14)
    night_env = Environment(hour=21)

    tests = [
        (subject, public_doc, day_env, "read"),
        (subject, secret_doc, day_env, "read"),
        (admin, secret_doc, day_env, "write"),
        (admin, secret_doc, night_env, "write"),
    ]

    for s, r, e, a in tests:
        decision = policy_allow(s, r, e, a)
        print(
            f"Kullanıcı={s.username} dept={s.department} -> kaynak={r.name} ({r.classification}), "
            f"saat={e.hour}, aksiyon={a} => izin: {decision}"
        )


if __name__ == "__main__":
    demo()
