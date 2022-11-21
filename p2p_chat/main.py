import argparse
import socket

from p2p_chat import server, client, spec, util

parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest="sub_func")

parser_run = subparser.add_parser("run")
parser_run.add_argument("module", help="Name of the module.", choices=['server', 'client'])

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
        util.print_usage()

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
