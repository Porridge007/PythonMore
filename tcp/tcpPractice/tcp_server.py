import socket


def main():
    # 1.create socket
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.bind port
    tcp_socket.bind(("127.0.0.1", 8080))

    # 3.listen
    tcp_socket.listen(128)

    while True:
        # 4.accept
        new_server_socket, client_addr = tcp_socket.accept()

        # 5.transfer
        # recv_data =tcp_socket.recv(1024)
        print(client_addr)

        recv_data = new_server_socket.recv(1024)
        print(recv_data.decode("utf-8"))

        new_server_socket.close()

    # 6.close socket
    tcp_socket.close()


if __name__ == '__main__':
    main()
