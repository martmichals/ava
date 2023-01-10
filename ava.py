import os
from chat.chat import Chat

if __name__ == '__main__':
    # Parse arguments

    # Chat needs to record the following:
    # Check for special commands, perform action in terminal
    # No support for abbreviations, character `
    # Must be launched on linux system

    # Launch chat
    chat = Chat()
    os.system('clear')
    while True:
        chat.fetch_human_chat('you')