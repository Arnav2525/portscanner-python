import time
from scanner.tcp_scanner import scan_tcp_ports
from scanner.udp_scanner import scan_udp_ports
from scanner.writer import write_results_to_file

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python main.py <IP_ADDRESS>")
        sys.exit(1)

    ip = sys.argv[1]
    start_port = 1
    end_port = 1024

    print(f"Scanning {ip} from port {start_port} to {end_port}...")

    start_time = time.time()

    tcp_results = scan_tcp_ports(ip, start_port, end_port)
    udp_results = scan_udp_ports(ip, start_port, end_port)

    elapsed_time = time.time() - start_time

    print(f"\nFound {len(tcp_results)} open TCP ports.")
    print(f"Found {len(udp_results)} open UDP ports.")

    write_results_to_file("scan-results.txt", ip, tcp_results, udp_results, elapsed_time)
