import threading

# Dictionary for Clients, Their usernames, and their chat Partner/Receiver
clients = dict()

def send(message):
    """
    Sends messages to the client
    :param message: Message string
    """
    username, msg = message.split(':')
    sender_client = clients[username].get('client')
    receiver = clients[username].get('receiver')
    receiver_client = clients[receiver].get('client')

    if receiver_client:
        receiver_client.send(f"{username}: {msg}".encode('ascii'))
        sender_client.send(f"(seen by {receiver})".encode('ascii'))


def list_clients(message, client):
    """
    Lists available users
    :param message: Message string
    :param client: Client object
    :return:
    """
    sender, msg = message.split(':')
    if sender:
        if len(clients) > 0:
            client.send(f"[SERVER] Online users: {', '.join(list(clients))}.".encode('ascii'))
        else:
            client.send(f"[SERVER] Nobody is online.".encode('ascii'))


def handle(username):
    """
    Handles the requests from the client
    :param username: Username of the client
    :return:
    """
    while True:
        client = clients[username]['client']
        try:
            # Broadcasting Messages
            message = client.recv(1024).decode('ascii')
            if '/exit' in message:
                clients.pop(username)
                client.close()
                break
            elif '/list' in message:
                list_clients(message, client)
            elif '/connect' in message:
                receiver = message.split('/connect')[-1].replace(' ', '')
                if receiver in clients:
                    clients[username]['receiver'] = receiver
                else:
                    print("[ERROR] Please choose an existing user from the online users list.")
            else:
                send(message)

        except:
            break


def receive(server):
    """
    Main function that receives the requests and sends them to the handle thread
    """
    while True:
        # Accept Connection
        client, address = server.accept()
        print("[CONNECTION] Connected with {}".format(str(address)))

        # Request And Store username
        client.send('USERNAME'.encode('ascii'))
        username = client.recv(1024).decode('ascii')

        clients[username] = dict(client=client, receiver=None)

        # Print And Broadcast username
        print("[REGISTER] User {} is registered".format(username))
        client.send('[CONNECTION] You are connected!'.format(username).encode('ascii'))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(username,))
        thread.start()
