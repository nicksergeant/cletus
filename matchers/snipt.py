from base import BaseMatcher

import random, requests, json


class SniptMatcher(BaseMatcher):

    name = 'snipt'

    def respond(self, message, user=None):

        r = requests.get('https://snipt.net/raw/586bf455bddee4d678d1409b8a7f112d/')
        data = json.loads(r.content)
        data = data[0]

        for group in data:
            if message.lower() in data[group]['matches']:
                message = random.choice(data[group]['responses'])
                if user:
                    message = user + ": " + message
                self.speak(str(message))
