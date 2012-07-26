from base import BaseMatcher


class SandwichMatcher(BaseMatcher):

    text = "fix me a whiskey"
    name = "whiskey"

    def respond(self, message, user=None):
        if self.text in message.lower():
            if 'sudo' in message:
                message = "used to could, can't no mo"
            else:
                message = "got a hankerin' for some juice, eh?"
            if user:
                message = user + ": " + message
            self.speak(message)
