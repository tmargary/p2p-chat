# Peer to peer console application

### Goals of the project

The clients are able to connect to the server and 
obtain a list of available clients. After obtaining this list, the client are able 
to connect to one other client on the list. The clients are capable of relaying text 
messages directly to one another.

### How to use the program?
- run `pip install .` from the root of the project
- Run `p2p_demo run server`
- From a different terminal, run `p2p_demo run client`
- (Optional) Continue adding as many clients as you need by running the command above.
- Follow the prompts.
- To get help about `p2p_demo`, run `p2p_demo --help`
- To get help about the main `run` functionality, run `p2p_demo run --help`

### To be improved
- Ability to exchange messages without further help from the server
- Implement a GUI
- Connect users outside the localhost via the Internet

### Demo
![ScreenShot](./screenshots/ss_0.png)
