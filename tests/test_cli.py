import pytest

from wcrtoolkit.cli import main
from wcrtoolkit.recon import port_scanner


def test_password_strength_command(capsys):
    exit_code = main(["password-strength", "Tr0ub4dor&3xyz"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "Score: 4/4 (very strong)" in captured.out


def test_password_strength_command_reports_issues(capsys):
    exit_code = main(["password-strength", "abc"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "Score: 0/4" in captured.out
    assert "- Password should be at least 8 characters long." in captured.out


def test_port_scan_command(monkeypatch, capsys):
    def fake_scan_ports(host, ports, timeout=1.0, *, connector=None):
        return [port_scanner.PortStatus(port=p, open=(p == 80)) for p in ports]

    monkeypatch.setattr("wcrtoolkit.cli.scan_ports", fake_scan_ports)

    exit_code = main(["port-scan", "example.com", "80", "443"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "example.com:80 open" in captured.out
    assert "example.com:443 closed" in captured.out


def test_no_command_exits_with_error():
    with pytest.raises(SystemExit):
        main([])
