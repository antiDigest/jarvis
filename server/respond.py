#!/Users/evamy/bot/bin/python

import json
from ai.intent.extract import getIntent
from . import despatch


def getResponse(command):
    intent = getIntent(command)

    print(json.dumps(intent, indent=2))

    intentName = intent["intent"]["intentName"]

    if intentName != None:
        # call the intent protocol here
        return despatch[intentName](intent["slots"])
    return
