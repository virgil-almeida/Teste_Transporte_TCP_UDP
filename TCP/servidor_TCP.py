import socket
import sys

# Cria o socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associa o socket a porta
server_address = ('localhost', 10000)
print ('Endereco servidor: %s porta: %s' % server_address)

sock.bind(server_address)
sock.listen(1)
try:
    while True:
        print ('\nAguardando mensagem')
        con, cliente = sock.accept()
        print("\nConectado com %s",cliente[0])
        # 1 - Recebe dados
        data = con.recv(1024)
        print ('Bytes recebidos %s de %s' %(len(data), cliente[0]))
        print (data.decode())
        
        if data:
            # 2 - Envia dados
            sent = con.send(data)
            print ('Bytes enviados %s de volta para %s' % (sent, cliente[0]))
        con.close()
except KeyboardInterrupt:
  print ("Saindo do Servidor")