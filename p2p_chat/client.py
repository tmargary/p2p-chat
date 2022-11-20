import socket
import threading
import spec


def receive():
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


def write():
    """
    Sends messages to server
    """
    while True:
        message = '{}:{}'.format(sender, input(':::'))
        client.send(message.encode('ascii'))


if __name__ == '__main__':
    # Prints usage on the terminal
    print("##########################################################")
    print("[USAGE]")
    print("/list: \t\t\t Lists available users")
    print("/connect [username]: \t Connects to the selected username")
    print("/exit: \t\t\t Disconnects the user")
    print("##########################################################")
    print('\n')

    # Choosing username
    sender = input("[PROMPT] Choose your username: ")

    # Connecting to Server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(spec.ADDRESS)

    # Starting thread for listening
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    # Starting thread for writing
    write_thread = threading.Thread(target=write)
    write_thread.start()

