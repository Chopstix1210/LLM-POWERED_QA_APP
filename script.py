#!/usr/bin/env python3

import os 
import sys 
import manai
import argparse
import time 

def loading_animation():
    animation_chars = ['-','\\','|','/']
    idx = 0

    while not animation_complete.is_set():
        print(animation_chars[idx % len(animation_chars)], end='\r')
        idx += 1
        time.sleep(0.1)

def parse_args():
    custom_usage = "manai [-c COMMAND] [-d DIALOG]"
    parser = argparse.ArgumentParser(description='manai command line tool', usage=custom_usage)
    #group = parser.add_mutually_exclusive_group(required=True)
    parser.add_argument('-c', '--command', help='Command or library you wish to get help with')
    parser.add_argument('-m', '--message', help='Message to send to manai')
    parser.add_argument('-l', '--login', help='Login or create account for manai', required=False, nargs='?')
    parser.add_argument('-d', '--dialog', help='Start a dialog with manai', required=False, nargs='?')
    parser.add_argument('command', nargs='?', help='Command or library you wish to get help with')
    return parser.parse_args()

def process_args(args):
    message = args.message
    login = args.login
    command = args.command
    dialog = args.dialog

    print(args)

    if login: 
        # go to login stuff
        pass 
    elif dialog:
        # start dialog 
        pass
    elif command and message:
        
        response = manai.command_message(command, message)
        formatted_response = f"manai: \n{'='*100}\n{response}\n{'='*100}"
        print(formatted_response)
    elif command:
        response = manai.manai_command(command)
        formatted_response = f"manai: \n{'='*100}\n{response}\n{'='*100}"
        print(formatted_response)
    elif message:
        response = manai.manai_message(message)
        formatted_response = f"manai: \n{'='*100}\n{response}\n{'='*100}"
        print(formatted_response)
    else: 
        print("Please use both -c and -m together to send a message to manai. Use '-h' for help.")

args = parse_args()
process_args(args)
