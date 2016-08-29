import json
import threading
from random import randint

import requests


# Tester which goes through randomly generated dialogue
class Tester(threading.Thread):
    def __init__(self, url, number):
        threading.Thread.__init__(self)
        self.url = url
        self.number = number

    # start thread
    def run(self):
        context = {}
        state = "init"
        session = ""
        end = False
        while not end:
            text = str(randint(0, 1))
            response = self.send_post(self.url, text, context, state, session)
            if response.json()["state"] == "END":
                end = True
            else:
                context = response.json()["context"]
                state = response.json()["state"]
                session = response.json()["session"]
        print("Tester " + str(self.number) + " ended successfully.")

    # sends post to Alquist and return its response
    def send_post(self, url, text, context, state, session):
        payload = {'text': text, 'context': context, 'state': state, 'session': session}
        headers = {'content-type': 'application/json'}
        return requests.post(url, data=json.dumps(payload), headers=headers)
