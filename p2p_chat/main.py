import argparse
import socket

from p2p_chat import server, client, spec

parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest="func_name")

parser_a = subparser.add_parser("run")
parser_a.add_argument("module", help="The name of the repo.", choices=['server', 'client'])
# parser_a.add_argument("-c", "--case_name", help="The name of the case.")

ARGS = parser.parse_known_args()[0]
KWARGS = vars(ARGS)


def main():

    module = KWARGS["module"]
    if module == "server":
        # Starting Server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(spec.ADDRESS)
        s.listen()
        print("[START] Server is listening...")
        server.receive(s)
    elif module == "client":
        # Prints usage on the terminal
        print('\n')
        print("##########################################################################")
        print("\t[USAGE]")
        print("\t/list: \t\t\t Lists available users")
        print("\t/connect [username]: \t Connects to the selected username")
        print("\t/exit: \t\t\t Disconnects the user")
        print("##########################################################################")
        print('\n')

        # Starting Server
        print("[START] Registering Client...")
        # Choosing username
        username = input("[PROMPT] Choose your username: ")

        # Connecting to Server
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c.connect(spec.ADDRESS)

        client.run_client(c, username)


if __name__ == '__main__':
    main()
