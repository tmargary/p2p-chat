import socket
import threading

from p2p_chat import spec


def receive(client, sender):
    """
    Listens to the server and sends username or prints the message
    """
    while True:
        try:
            # Receive Message From Server
            # If 'USERNAME' Send username
            message = client.recv(1024).decode('ascii')
            if message == 'USERNAME':
                client.send(sender.encode('ascii'))
            else:
                print(message)
        except:
            print("[ERROR] An error occurred! Try again.")
            break


def write(client, sender):
    """
    Sends messages to server
    """
    while True:
        message = '{}:{}'.format(sender, input(':::'))
        client.send(message.encode('ascii'))


def run_client(c, username):

    # Starting thread for listening
    receive_thread = threading.Thread(target=receive, args=(c, username))
    receive_thread.start()

    # Starting thread for writing
    write_thread = threading.Thread(target=write, args=(c, username))
    write_thread.start()

