import socket

host = ''
port = 30000
sock = socket.socket(socket.AF_INET, socket.SOCK_DTGRAM)
sock.connect((HOST, PORT))
while True:
    s = raw_input()
    if s == '':
        continue
    sock.send(s)
    result = sock.recv(4096)
    sock.close()
    print "Получено:", result
