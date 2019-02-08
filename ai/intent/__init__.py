#!/Users/evamy/bot/bin/python

import io
import json
from snips_nlu import SnipsNLUEngine

with io.open("samples/extract_intent.json") as f:
    intents_dataset = json.load(f)

nlu_engine = SnipsNLUEngine()
nlu_engine.fit(intents_dataset)
