import socket
from .service_mapper import get_service_name

def scan_tcp_ports(ip: str, start_port: int, end_port: int) -> list[str]:
    open_ports = []
    for port in range(start_port, end_port + 1):
        print(f"Scanning TCP port {port}...")  # ✅ Debug print
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((ip, port))
            if result == 0:
                service = get_service_name(port)
                open_ports.append(f"TCP Port {port} is open ({service})")
    return open_ports
