# import socket
# import multiprocessing
#
#
# def handle_connection(client_socket):
#     """
#     子进程处理连接过来的客户端
#     :param client_socket: 新客户端socket
#
#     """
#     print('start a new process!')
#     while True:
#         rece_data = client_socket.recvfrom(1024)
#         print(rece_data[0].decode())
#         if rece_data[0].decode().__len__() == 0:
#             break
#         client_socket.send(rece_data[0])
#     print('closed this socket')
#     client_socket.close()
#
#
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind(('', 8899))
# server_socket.listen(100)
# while True:
#     new_socket, address = server_socket.accept()
#     handle_process = multiprocessing.Process(target=handle_connection, args=(new_socket, ))
#     handle_process.start()
