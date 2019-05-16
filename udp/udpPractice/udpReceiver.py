import socket


def udp_communicate():
    # create udp socket-
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    local_addr = ("", 8080)
    udp_socket.bind(local_addr)

    while True:
        recv_data = udp_socket.recvfrom(1024)
        recv_msg = recv_data[0]
        send_addr = recv_data[1]
        print("recv_msg: " + str(recv_msg.decode("utf-8")) + " from " + str(send_addr))
        if str(recv_msg.decode("utf-8")) == "exit":
            break

    # close socket
    udp_socket.close()


if __name__ == '__main__':
    udp_communicate()
