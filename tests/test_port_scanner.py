import pytest

from wcrtoolkit.recon.port_scanner import PortStatus, scan_port, scan_ports


class _FakeConnection:
    def __enter__(self):
        return self

    def __exit__(self, *exc_info):
        return False


def make_connector(open_ports):
    def connector(address, timeout=None):
        _, port = address
        if port in open_ports:
            return _FakeConnection()
        raise ConnectionRefusedError(f"connection refused on port {port}")

    return connector


def test_scan_port_open():
    connector = make_connector({80})
    assert scan_port("example.com", 80, connector=connector) == PortStatus(port=80, open=True)


def test_scan_port_closed():
    connector = make_connector({80})
    assert scan_port("example.com", 22, connector=connector) == PortStatus(port=22, open=False)


def test_scan_ports_multiple():
    connector = make_connector({22, 443})
    results = scan_ports("example.com", [22, 80, 443], connector=connector)
    assert results == [
        PortStatus(port=22, open=True),
        PortStatus(port=80, open=False),
        PortStatus(port=443, open=True),
    ]


@pytest.mark.parametrize("port", [0, -1, 65536, 100000])
def test_scan_port_invalid_port_raises(port):
    with pytest.raises(ValueError):
        scan_port("example.com", port, connector=make_connector(set()))
