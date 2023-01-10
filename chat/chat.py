import os
from datetime import datetime

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Message:

    def __init__(self, uid: str, text: str, timestamp: datetime, human: bool):
        self.text = text
        self.text_length = len(text)
        self.uid = uid
        self.timestamp = timestamp
        self.human = human

class Chat:
    SYSTEM_ID = 'sys'

    def __init__(self):
        self.log = []
        self.uids = set(Chat.SYSTEM_ID)
        self.longest_uid = len(Chat.SYSTEM_ID)

    @property
    def last_human_message(self):
        for message in reversed(self.log):
            if message.human: return message

    def get_prefix(self, uid: str):
        return f'{uid:>{self.longest_uid}}> '

    def print_warning(self, warning: str):
        print(f'{self.get_prefix(Chat.SYSTEM_ID)}{bcolors.WARNING}{warning}{bcolors.ENDC}')

    def clear(self, command: str):
        os.system('clear')
        if len(self.log) > 0:
            message = self.log[-1]
            print(f'{self.get_prefix(message.uid)}{message.text}')

    def fetch_human_chat(self, uid: str) -> bool:
        # Supported chat commands
        commands = {
            'clear': self.clear
        }

        # Update the UID data structures
        if uid not in self.uids:
            self.uids.add(uid)
            self.longest_uid = max(self.longest_uid, len(uid))

        # Get message from the terminal
        try:
            text = input(self.get_prefix(uid))
            text = text.encode('ascii', 'strict').decode('ascii')
        except UnicodeEncodeError:
            self.print_warning('Please restrict your messages to ASCII characters.')
            return False

        # Check for commands
        if '`' in text:
            if text[0] != '`' or text.count('`') > 1: 
                self.print_warning('To run a command, type a message with ` as the first character, followed by the command. For example: "`clear"')
            if text[1:] not in commands:
                self.print_warning(f'Invalid command. Valid commands: {list(commands.keys())}.')
            commands[text[1:]](text[1:])
            return False

        # Append the message to the log
        self.log.append(Message(uid, text, datetime.now(), True))
        return True

    def add_ai_response(self, uid: str, text: str):
        # Update the UID data structures
        if uid not in self.uids:
            self.uids.add(uid)
            self.longest_uid = max(self.longest_uid, len(uid))

        # Print out the message
        print(f'{self.get_prefix(uid)}{text}')

        # Add message to the log
        self.log.append(Message(uid, text, datetime.now(), False))

    def save(self, filepath: str):
        # Save the chat as a JSON file
        raise NotImplementedError

    # TODO: Add up arrow support to grab the last answer typed

