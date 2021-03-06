import socket
import sys
import select
import threading

def check_input(s):
    answer = True
    if s == '':
        answer = False
    count_space = 0
    for l in s:
        if l == ' ':
            count_space += 1
    if count_space == len(s):
        answer = False
    return answer
       
def get_message(sock):
    while True:
        message = sock.recvfrom(4064)[0]
        print message

def print_message(s):
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'
    print CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE
    print 'You: ' + s


def main():
    print '=======================Let\'s chat=======================' 
    client_name = raw_input('Write your name: ')

    host = ''
    port = 30000
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    new_thread = threading.Thread(target = get_message, args = (sock,))
    new_thread.start()
    while True:
        s = raw_input()
        print_message(s)
        if check_input(s):
            message = client_name + ': ' + s
            sock.sendto(message, (host, port))
       
if __name__ == '__main__':
    main()
