# Peer to peer console application

### Goals of the project

This is a peer to peer console chat application. The clients are able to connect to the server via TCP socket
connections and  obtain the list of available clients. Afterwards, the client can connect to one other client 
on the list and exchange text messages directly to one another.

### Installation
- run `pip install .` from the root of the project
- Run `p2p_demo run server`
- Run `p2p_demo run client` (from a different terminal)
- _(Optional)_ Continue adding as many clients as you need by running the command above.
- Follow the prompts.
- _(Optional)_ To get help about `p2p_demo`, run `p2p_demo --help`
- _(Optional)_ To get help about the main `run` functionality, run `p2p_demo run --help`

### To be improved
- Ability to exchange messages without further help from the server
- Implement a GUI
- Connect users outside the localhost via the Internet
- Test the package on Windows (tested only on Linux)
- Implement tests

### Demo screenshot
![ScreenShot](./screenshots/ss_0.png)

### Requirements
- Python >3.7