import socket
import sys

# Cria socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_address = ('localhost', 10000)
message = 'IFMG Betim. Irei repetir.'

sock.connect(server_address)

try:
    # 1 - Envia dados
    print ('enviando "%s"' %message)
    sent = sock.send(message.encode())

    # 2 - Recebe dados
    print ('Aguardando...')
    data = sock.recv(1024)
    print ('recebido "%s"' %data.decode())

finally:
    print ('fechando o socket')
    sock.close()
