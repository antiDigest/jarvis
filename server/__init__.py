#!/Users/evamy/bot/bin/python

from systems.weather import weatherProtocol
from systems.volume import volumeProtocol

despatch = {"weatherProtocol": weatherProtocol,
            "volumeProtocol": volumeProtocol}
