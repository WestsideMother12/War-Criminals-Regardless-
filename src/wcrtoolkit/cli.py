"""Command-line interface for wcrtoolkit."""

from __future__ import annotations

import argparse
import sys
from typing import Sequence

from .recon.port_scanner import scan_ports
from .security.password_strength import evaluate_password


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="wcrtoolkit", description="Authorized security-testing toolkit")
    subparsers = parser.add_subparsers(dest="command", required=True)

    pw_parser = subparsers.add_parser("password-strength", help="Evaluate password strength")
    pw_parser.add_argument("password")

    scan_parser = subparsers.add_parser("port-scan", help="Scan TCP ports on a host")
    scan_parser.add_argument("host")
    scan_parser.add_argument("ports", type=int, nargs="+")
    scan_parser.add_argument("--timeout", type=float, default=1.0)

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "password-strength":
        result = evaluate_password(args.password)
        print(f"Score: {result.score}/4 ({result.label})")
        for issue in result.issues:
            print(f"- {issue}")
        return 0

    if args.command == "port-scan":
        results = scan_ports(args.host, args.ports, timeout=args.timeout)
        for status in results:
            state = "open" if status.open else "closed"
            print(f"{args.host}:{status.port} {state}")
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
