"""Basit bir RBAC (Role-Based Access Control) demo modülü.

Küçük bir kullanıcı, rol ve izin tablosu ile erişim kararı verir.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Set


@dataclass
class User:
    username: str
    roles: List[str]


# Rol → izin seti (resource:action formatında)
ROLE_PERMISSIONS: Dict[str, Set[str]] = {
    "admin": {"video:read", "video:write", "user:manage"},
    "editor": {"video:read", "video:write"},
    "viewer": {"video:read"},
}


def has_permission(user: User, permission: str) -> bool:
    """Kullanıcının verilen izne sahip olup olmadığını kontrol eder."""

    user_perms: Set[str] = set()
    for role in user.roles:
        user_perms |= ROLE_PERMISSIONS.get(role, set())
    return permission in user_perms


def demo() -> None:
    """RBAC karar mekanizmasını gösteren basit bir demo.

    Çalıştırmak için:
        python -m src.access_control.rbac_demo
    """

    users = [
        User(username="ali", roles=["viewer"]),
        User(username="ayse", roles=["editor"]),
        User(username="admin", roles=["admin"]),
    ]

    test_perm = "video:write"
    for u in users:
        print(f"Kullanıcı: {u.username:5s} | Roller: {u.roles} | '{test_perm}' yetkisi: {has_permission(u, test_perm)}")


if __name__ == "__main__":
    demo()
