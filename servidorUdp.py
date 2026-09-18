import socket

servidor = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)

servidor.bind(("localhost", 5000))

print("servidor UDP aguardando mensagens... ")

dados, endereco = servidor.recvfrom(1024)

mensagem = dados.decode()

print("cliente: ", endereco)
print("mensagem recebida:", mensagem)

resposta = "mensagem recebida pelo servidor UDP"

servidor.sendto(
    resposta.encode(),
    endereco
)

servidor.close
