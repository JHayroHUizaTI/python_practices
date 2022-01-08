import socket
from IPy import IP

class PortScan():
    def __init__(self, target, port_num):
        self.target = target
        self.port_num = port_num
    def check_ip(self,ip):
        try:
            IP(ip)
        except ValueError:
            return socket.gethostbyname(ip)

    def get_banner(self,s):
        return s.recv(1024)
    def scan(self,target):
        converted_ip = check_ip(target)
        print('\n' + '[ Scanning Target]' + str(target))
        for port in range(1,100):
            scan_port(converted_ip, port)
            
    def scan_port(self,ipaddress, port):
        try:
            #Create a socket object using socket.socket()
            sock = socket.socket()
            sock.settimeout(0,5)
            """
            To establish a connection to the server and initiate
            the three-way handshake
            """ 
            sock.connect((ipaddress, port))
            try:
                banner = get_banner(sock)
                print(f"[+] port {port} : {banner.decode().strip('\n')}")
            except:
                print(f'Open port {port}')
        except:
            pass
#port_num = input('Enter number of ports that you want to scan')
if __name__ == "__main__":
    targets = input("[+] Enter target to scan: ")
    if ', ' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '))
    else:
        scan(targets)