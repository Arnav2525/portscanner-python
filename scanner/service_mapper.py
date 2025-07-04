import socket

def get_service_name(port, protocol='tcp'):
    """
    Returns the common service name for a given port.
    If the port is not recognized, returns 'Unknown Service'.
    """
    common_services = {
        20: "FTP Data", 21: "FTP Control", 22: "SSH", 23: "Telnet", 25: "SMTP",
        53: "DNS", 67: "DHCP Server", 68: "DHCP Client", 69: "TFTP", 80: "HTTP",
        110: "POP3", 123: "NTP", 137: "NetBIOS Name", 138: "NetBIOS Datagram",
        139: "NetBIOS Session", 143: "IMAP", 161: "SNMP", 162: "SNMP Trap",
        179: "BGP", 443: "HTTPS", 445: "SMB", 465: "SMTPS", 514: "Syslog",
        587: "SMTP (submission)", 631: "IPP (printing)", 993: "IMAPS",
        995: "POP3S", 3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL",
        5900: "VNC", 8080: "HTTP-Alt"
    }
    if port in common_services:
        return common_services[port]
    try:
        return socket.getservbyport(port, protocol)
    except OSError:
        return "Unknown Service"
