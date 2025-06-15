import socket
target=input('Enter the IP addres to scan:')
port_range=input("Enter the port range to scan:")
start_port,end_port=map(int,port_range.split('-'))
print(f"\nScanning TCP ports {start_port} to {end_port} on {target}")
for port in range(start_port,end_port + 1):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(1)
    result=s.connect_ex((target,port))
    if result==0:
        print(f"TCP {port} is open")
    else:
        print(f"TCP {port} is closed")
print(f"Scanning UDP ports {start_port} to {end_port}on {target  }")
for port in range(start_port,end_port + 1):
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.settimeout(1)
        s.sendto(b'',(target,port))
        data,addr=s.recvfrom(1024)
        print(f"UDP port {port} is open or response")
    except socket.timeout:
        print(f"UDP PORT {port} is Filitered or closed (no response)")
    except Exception as e:
        print(f"Error on the UDP port{port} :{e}")
    finally:
        s.close()
      