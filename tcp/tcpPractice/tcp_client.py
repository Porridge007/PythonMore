import socket


def main():
    # 1.create socket
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.connect server
    tcp_socket.connect(("127.0.0.1", 8080))

    # 3.transfer data
    send_data = input("input what you want to send\n")
    tcp_socket.send(send_data.encode("utf-8"))

    # 4.close socket
    tcp_socket.close()


if __name__ == '__main__':
    main()
