#!/Users/evamy/bot/bin/python

import random

cannotMessages = ["I'm sorry I can't help with that yet",
                  "Sorry, I'm not yet trained for this", "Sorry, I cannot help with this"]


def cannotDoThatYet():
    return cannotMessages[random.randint(0, len(cannotMessages))]
