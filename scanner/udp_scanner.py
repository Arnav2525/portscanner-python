import socket
from .service_mapper import get_service_name

def send_dns_query(ip):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(1)
        dns_query = bytearray([
            0x12, 0x34, 0x01, 0x00, 0x00, 0x01,
            0x00, 0x00, 0x00, 0x00,
            0x07, ord('e'), ord('x'), ord('a'), ord('m'), ord('p'), ord('l'), ord('e'),
            0x03, ord('c'), ord('o'), ord('m'), 0x00,
            0x00, 0x01, 0x00, 0x01
        ])
        sock.sendto(dns_query, (ip, 53))
        response, _ = sock.recvfrom(512)
        sock.close()
        return True
    except:
        return False

def send_ntp_query(ip):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(1)
        ntp_data = bytearray(48)
        ntp_data[0] = 0x1B
        sock.sendto(ntp_data, (ip, 123))
        response, _ = sock.recvfrom(48)
        sock.close()
        return True
    except:
        return False

def scan_udp_ports(ip, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        print(f"Scanning UDP port {port}...")  # ✅ Debug print
        if port == 53 and send_dns_query(ip):
            service = get_service_name(port)
            open_ports.append(f"UDP Port {port} is open ({service})")
        elif port == 123 and send_ntp_query(ip):
            service = get_service_name(port)
            open_ports.append(f"UDP Port {port} is open ({service})")
        else:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.settimeout(1)
                sock.sendto(b'\x00', (ip, port))
                sock.recvfrom(1024)
                service = get_service_name(port)
                open_ports.append(f"UDP Port {port} is open ({service})")
            except socket.timeout:
                pass
            except:
                pass
            finally:
                sock.close()
    return open_ports
