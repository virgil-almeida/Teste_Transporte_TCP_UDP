import socket
import sys

# Cria socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


server_address = ('localhost', 10000)
message = 'IFMG Betim. Irei repetir.'

try:

    # 1 - Envia dados
    print ('enviando "%s"' %message)
    sent = sock.sendto(message.encode(), server_address)

    # 2 - Recebe dados
    print ('Aguardando...')
    data, server = sock.recvfrom(4096)
    print ('recebido "%s"' %data.decode())

finally:
    print ('fechando o socket')
    sock.close()