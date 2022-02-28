import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ports = []
host = input("Please enter the ip Address: ")

port_num = int(input("How many port you want to scan: "))

for i in range(port_num):
    port = input("Please enter the port the that you want to scan: ")
    ports.append(port)

for port in ports:
    if sock.connect_ex((host,int(port))):
        sock.settimeout(5)
        print(f"The port {port} is closed")
    else:
        sock.settimeout(5)
        print(f"The port {port} is opened")
