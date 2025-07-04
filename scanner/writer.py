import datetime

def write_results_to_file(filename, ip, tcp_results, udp_results, time_taken):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f"Port Scan Report - {datetime.datetime.now()}\n")
            file.write(f"Target IP: {ip}\n")
            file.write(f"Total Time Taken: {time_taken:.2f} seconds\n")
            file.write("-" * 40 + "\n\n")

            file.write("Open TCP Ports:\n")
            if tcp_results:
                for line in tcp_results:
                    file.write(line + '\n')
            else:
                file.write("None found.\n")

            file.write("\nOpen UDP Ports:\n")
            if udp_results:
                for line in udp_results:
                    file.write(line + '\n')
            else:
                file.write("None found.\n")

        print(f"\n✅ Scan results saved to {filename}")
    except Exception as e:
        print(f"❌ Error writing results to file: {e}")
