#!/usr/local/bin/python3
import time
import sys
import html
from MeteorClient import MeteorClient

client = MeteorClient('ws://localhost:3000/websocket')
password = "password"

def connected():
    print('*** CONNECTED TO TERMINAL-STREAMER ***')
    client.login("admin", password.encode('utf-8'))

def insert_callback(error, data):
    if error:
        print("error insert_callback:")
        print(error)

def logged_in(error):
    arguments()
    terminalStream()


def terminalStream():
    client.insert('terminal', {'content': time.strftime("<div class=\"blue\">[%Y-%m-%d %H:%M:%S]</div>", time.gmtime())}, callback=insert_callback)
    for line in sys.stdin:
        print(line, end="")
        client.insert('terminal', {'content': html.escape(line)}, callback=insert_callback)

def arguments():
    for arg in sys.argv[1:]:
        if(arg == "clear"):
            client.call('clearTerminal', [])

client.on('connected', connected)
client.on('logged_in', logged_in)

client.connect()

# (sort of) hacky way to keep the client alive
# ctrl + c to kill the script
while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        break