import socket


def udp_communicate():
    # create udp socket-
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        # use socket to transfer data
        dest_addr = ("127.0.0.1", 8080)
        send_data = input("Enter your input\n")
        if send_data == 'exit':
            break
        udp_socket.sendto(send_data.encode('utf-8'), dest_addr)

    # close socket
    udp_socket.close()


if __name__ == '__main__':
    udp_communicate()
