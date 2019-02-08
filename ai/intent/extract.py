#!/Users/evamy/bot/bin/python

import json
# from __init__ import nlu_engine
from . import nlu_engine

def getIntent(sentence):
    parsing = nlu_engine.parse(sentence)
    #print(json.dumps(parsing, indent=2))
    return parsing
