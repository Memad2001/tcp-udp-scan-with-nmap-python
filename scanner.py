import nmap

scanner = nmap.PortScanner()

print("Welcome to scanner tool!")
print("<",50*'-',">")

ip = input("Please enter the Ip address you want to scan: ")

type_of_scan = input("""chose the type of scan:\n
                        [1] SYN ACK scan
                        [2] UDP scan
                        [3] Comprehensive scan                        
""")

if type_of_scan == '1':
    scanner.scan(ip,'1-1024','-v -sS')
    print("State: ",scanner[ip].state())
    print("Ports:",scanner[ip].all_protocols())
    print("open ports: ",scanner[ip]['tcp'].keys())
elif type_of_scan == '2':
    scanner.scan(ip,'1-1024','-v -sU')
    print("State:",scanner[ip].state())
    print("Portocol:",scanner[ip].all_protocols())
    print("Open ports:",scanner[ip]['udp'].keys())
elif type_of_scan == '3':
    scanner.scan(ip,'1-1024','-v -sS  -sV -sC -O -A')
    print("State:",scanner[ip].state())
    print("Portocol:",scanner[ip].all_protocols())
    print("Open ports:",scanner[ip]['tcp'].keys())
elif type_of_scan >= 4:
    print("Please enter a valid value!")
    