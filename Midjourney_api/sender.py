# import requests
# import json
# import time
# import re
# import argparse
# import sys

# class Sender:

#     def __init__(self, 
#                  params):
        
#         self.params = params
#         self.sender_initializer()

#     def sender_initializer(self):

#         with open(self.params, "r") as json_file:
#             params = json.load(json_file)

#         self.channelid=params['channelid']
#         self.authorization=params['authorization']
#         self.application_id = params['application_id']
#         self.guild_id = params['guild_id']
#         self.session_id = params['session_id']
#         self.version = params['version']
#         self.id = params['id']
#         self.flags = params['flags']
        
        
#     def send(self, prompt):
#         header = {
#             'authorization': self.authorization
#         }
        
#         prompt = prompt.replace('_', ' ')
#         prompt = " ".join(prompt.split())
#         prompt = re.sub(r'[^a-zA-Z0-9\s]+', '', prompt)
#         prompt = prompt.lower()

#         payload = {'type': 2, 
#         'application_id': self.application_id,
#         'guild_id': self.guild_id,
#         'channel_id': self.channelid,
#         'session_id': self.session_id,
#         'data': {
#             'version': self.version,
#             'id': self.id,
#             'name': 'imagine',
#             'type': 1,
#             'options': [{'type': 3, 'name': 'prompt', 'value': str(prompt) + ' ' + self.flags}],
#             'attachments': []}
#             }
        
#         r = requests.post('https://discord.com/api/v9/interactions', json = payload , headers = header)
#         while r.status_code != 204:
#             r = requests.post('https://discord.com/api/v9/interactions', json = payload , headers = header)

#         print('prompt [{}] successfully sent!'.format(prompt))

# def parse_args(args):
    
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--params',        help='Path to discord authorization and channel parameters', required=True)
#     parser.add_argument('--prompt',           help='prompt to generate', required=True)
        
#     return parser.parse_args(args)


# if __name__ == "__main__":

#     args = sys.argv[1:]
#     args = parse_args(args)
#     params = args.params
#     prompt = args.prompt

#     sender = Sender(params)
#     sender.send(prompt)
import requests
import json
import time
import re
import argparse
import sys
from dotenv import load_dotenv
import os

class Sender:

    def __init__(self):
        load_dotenv()  # Load environment variables from .env file
        self.sender_initializer()

    def sender_initializer(self):
        self.channelid = os.getenv('DISCORD_CHANNEL_ID')
        self.authorization = os.getenv('AUTH')
        self.application_id = os.getenv('DISCORD_APPLICATION_ID')
        self.guild_id = os.getenv('DISCORD_GUILD_ID')
        self.session_id = os.getenv('DISCORD_SESSION_ID')
        self.version = os.getenv('DISCORD_VERSION')
        self.id = os.getenv('DISCORD_ID')
        self.flags = os.getenv('DISCORD_FLAGS')

    def send(self, prompt):
        header = {
            'authorization': self.authorization
        }

        prompt = prompt.replace('_', ' ')
        prompt = " ".join(prompt.split())
        prompt = re.sub(r'[^a-zA-Z0-9\s]+', '', prompt)
        prompt = prompt.lower()

        payload = {
            'type': 2,
            'application_id': self.application_id,
            'guild_id': self.guild_id,
            'channel_id': self.channelid,
            'session_id': self.session_id,
            'data': {
                'version': self.version,
                'id': self.id,
                'name': 'imagine',
                'type': 1,
                'options': [{'type': 3, 'name': 'prompt', 'value': str(prompt) + ' ' + self.flags}],
                'attachments': []
            }
        }

        r = requests.post('https://discord.com/api/v9/interactions', json=payload, headers=header)
        while r.status_code != 204:
            r = requests.post('https://discord.com/api/v9/interactions', json=payload, headers=header)

        print('prompt [{}] successfully sent!'.format(prompt))

def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--prompt', help='prompt to generate', required=True)
    return parser.parse_args(args)

if __name__ == "__main__":
    args = sys.argv[1:]
    args = parse_args(args)
    prompt = args.prompt

    sender = Sender()
    sender.send(prompt)
