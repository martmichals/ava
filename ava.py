import os
from chat.chat import Chat
from transformers import pipeline, set_seed

def generate_response(generator, human_message):
    # TODO: Fine tune the generator for conversation
    generated_text = generator(human_message.text, max_length=50)[0]['generated_text']
    return generated_text

if __name__ == '__main__':
    # Parse arguments

    # Chat needs to record the following:
    # Check for special commands, perform action in terminal
    # No support for abbreviations, character `
    # Must be launched on linux system

    # Instantiate chat and generator
    chat = Chat()
    generator = pipeline('text-generation', model='gpt2-xl', device=0)

    # Launch chat
    os.system('clear')
    while True:
        while not chat.fetch_human_chat('you'): pass
        # chat.add_ai_response('ava', generate_response(generator, chat.last_human_message)) 
        chat.add_ai_response('ava', 'artificial response') 