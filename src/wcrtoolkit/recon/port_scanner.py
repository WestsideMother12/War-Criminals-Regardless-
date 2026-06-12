"""Basic TCP connect-scan utilities.

Only use against hosts and ports you own or have explicit permission to test.
"""

from __future__ import annotations

import socket
from dataclasses import dataclass
from typing import Callable, Iterable


@dataclass(frozen=True)
class PortStatus:
    port: int
    open: bool


Connector = Callable[..., object]


def scan_port(host: str, port: int, timeout: float = 1.0, *, connector: Connector | None = None) -> PortStatus:
    """Check whether a single TCP port is open on `host`.

    `connector` is an injectable socket factory used for testing; it defaults
    to `socket.create_connection`.
    """
    if not 0 < port < 65536:
        raise ValueError(f"Port must be between 1 and 65535, got {port}")

    connector = connector or socket.create_connection
    try:
        with connector((host, port), timeout=timeout):
            return PortStatus(port=port, open=True)
    except OSError:
        return PortStatus(port=port, open=False)


def scan_ports(
    host: str, ports: Iterable[int], timeout: float = 1.0, *, connector: Connector | None = None
) -> list[PortStatus]:
    """Scan multiple ports on a host, returning a list of PortStatus."""
    return [scan_port(host, port, timeout=timeout, connector=connector) for port in ports]
