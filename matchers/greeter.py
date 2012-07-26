from base import BaseMatcher

import random


class GreetingMatcher(BaseMatcher):

    name = 'greeter'
    greetings = [
        'all: morning',
        'all: howdy',
        'all: greetings',
        'all: hello',
        'all: hey',
        'all: hi',
        'hi',
        'hey',
        'hello',
        'sup',
        'howdy',
    ]

    responses = [
        'how y\'all doin',
        'yeeeaasiree',
        'sup, yankee',
        'howdy tater',
        'how do?',
        'what\'s good?',
        'yeap',
        'yeallow',
    ]

    def respond(self, message, user=None):
        if message.lower() in self.greetings:
            message = random.choice(self.responses)
            if user:
                message = user + ": " + message
            self.speak(message)
