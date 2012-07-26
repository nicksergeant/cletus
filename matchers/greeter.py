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
        'howdy',
    ]
    leavings = [
        'leaving',
        'done for the day',
        'stopping for the day',
        'stopping here',
    ]

    def respond(self, message, user=None):
        if message.lower() in self.greetings:
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
            message = random.choice(responses)
            if user:
                message = user + ": " + message
            self.speak(message)

        if message.lower() in self.leavings:
            laters = [
                'catch ya on the flipside',
                'later varmint',
                'skedaddle',
                'y\'all come back now, ya-hear',
            ]
            message = random.choice(laters)
            if user:
                message = user + ": " + message
            self.speak(message)

        if 'sup cletus' in message.lower():
            sups = [
                'Them fellas done killed a 9 point yesterday morn',
                'To get to their house, go up the holler, follow the creck, past to old oak and turn north',
                'If you want to get something done, find a busy man. There\'s a reason he\'s busy',
            ]
            message = random.choice(sups)
            if user:
                message = user + ": " + message
            self.speak(message)

        if 'how long' in message.lower():
            message = 'Ima figurin\' it\'ll be two days'
            if user:
                message = user + ": " + message
            self.speak(message)
