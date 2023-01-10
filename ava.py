import os
from chat.chat import Chat

if __name__ == '__main__':
    # Parse arguments

    # Chat needs to record the following:
    # Time of message
    # Length of message (validation checks for length of model)
    # Message contents (restrict to ASCII to start)
    # Check for special commands, perform action in terminal
    # No support for abbreviations, character `
    # Must be launched on linux system

    # Launch chat
    os.system('clear')
    while True:
        user_message = input('you> ')
        response = "-Ava's response-"
        print(f'ava> {response}')