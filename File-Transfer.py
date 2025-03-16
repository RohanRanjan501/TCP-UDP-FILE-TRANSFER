import socket
import os

# TCP Server

def tcp_server(host='127.0.0.1', port=5001, buffer_size=1024):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"[TCP] Server listening on {host}:{port}")

    conn, addr = server_socket.accept()
    print(f"[TCP] Connection from {addr}")

    filename = conn.recv(buffer_size).decode()
    if os.path.exists(filename):
        conn.send(b'EXIST')
        with open(filename, 'rb') as f:
            data = f.read(buffer_size)
            while data:
                conn.send(data)
                data = f.read(buffer_size)
        print(f"[TCP] File {filename} sent successfully.")
    else:
        conn.send(b'NOFILE')

    conn.close()
    server_socket.close()

# TCP Client

def tcp_client(server_host='127.0.0.1', port=5001, filename='test.txt', buffer_size=1024):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, port))
    client_socket.send(filename.encode())

    response = client_socket.recv(buffer_size).decode()
    if response == 'EXIST':
        with open('received_' + filename, 'wb') as f:
            data = client_socket.recv(buffer_size)
            while data:
                f.write(data)
                data = client_socket.recv(buffer_size)
        print(f"[TCP] File {filename} received successfully.")
    else:
        print("[TCP] File not found on server.")

    client_socket.close()

# UDP Server

def udp_server(host='127.0.0.1', port=5002, buffer_size=1024):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"[UDP] Server listening on {host}:{port}")

    while True:
        filename, client_addr = server_socket.recvfrom(buffer_size)
        filename = filename.decode()
        print(f"[UDP] Requested file: {filename} from {client_addr}")

        if os.path.exists(filename):
            server_socket.sendto(b'EXIST', client_addr)
            with open(filename, 'rb') as f:
                data = f.read(buffer_size)
                while data:
                    server_socket.sendto(data, client_addr)
                    data = f.read(buffer_size)
            print(f"[UDP] File {filename} sent successfully.")
        else:
            server_socket.sendto(b'NOFILE', client_addr)

# UDP Client

def udp_client(server_host='127.0.0.1', port=5002, filename='test.txt', buffer_size=1024):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto(filename.encode(), (server_host, port))

    response, _ = client_socket.recvfrom(buffer_size)
    if response.decode() == 'EXIST':
        with open('received_' + filename, 'wb') as f:
            data, _ = client_socket.recvfrom(buffer_size)
            while data:
                f.write(data)
                client_socket.settimeout(2)  # Timeout for UDP
                try:
                    data, _ = client_socket.recvfrom(buffer_size)
                except socket.timeout:
                    break
        print(f"[UDP] File {filename} received successfully.")
    else:
        print("[UDP] File not found on server.")

    client_socket.close()

if __name__ == "__main__":
    choice = input("Run (tcp_server/tcp_client/udp_server/udp_client): ")
    if choice == "tcp_server":
        tcp_server()
    elif choice == "tcp_client":
        filename = input("Enter filename to download: ")
        tcp_client(filename=filename)
    elif choice == "udp_server":
        udp_server()
    elif choice == "udp_client":
        filename = input("Enter filename to download: ")
        udp_client(filename=filename)
    else:
        print("Invalid choice.")
