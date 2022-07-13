import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind((HOST, PORT))
tcp.listen(1)
print("listado na porta ", PORT) # Port to listen on (non-privileged ports are > 1023)

def close(): 
    tcp.close()
    print("Servidor encerrado")

def main():
    while True:
        conn, addr = tcp.accept()
        print("Conectado a: ", addr)
        while True:
            data = conn.recv(1024)
            print(data.decode())
            if not data:
                break
            conn.sendall(data)
        tcp.close()
        print("Conecxão encerrada")

main()