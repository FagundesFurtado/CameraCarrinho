import socket
HOST = '192.168.1.109'  # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
print ('Para sair use CTRL+X\n')
msg = input()
while msg != 'x':
    udp.sendto (str(msg).encode('utf-8'), dest)
    msg = input()
udp.close()
