import socket
import sys

# Cria o socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Associa o socket a porta
server_address = ('localhost', 10000)
print ('Endereco servidor: %s porta: %s' % server_address)
sock.bind(server_address)
try:
    while True:
        print ('\nAguardando mensagem')
        # 1 - Recebe dados
        data, address = sock.recvfrom(4096)
        print ('Bytes recebidos %s de %s' % (len(data), address))
        print (data.decode())
        
        if data:
            # 2 - Envia dados
            sent = sock.sendto(data, address)
            print ('Bytes enviados %s de volta para %s' % (sent, address))
except KeyboardInterrupt:
  print ("Saindo do Servidor")