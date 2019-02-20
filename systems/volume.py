#!/Users/evamy/bot/bin/python
# ################################################################################################
#       
#         Handles all commands that refer to manipulating the volume of the system
# 
# ################################################################################################
# ################################################################################################
# 
#         @version 0: simple command to manipulate volume
# 
#         @author: Antriksh Agarwal
# 
# ################################################################################################



import osascript
import math

from server.error import cannotDoThatYet
from AppKit import NSBeep


def volumeProtocol(slots):
    '''
        The volume protocol is a switch statement on the identified intent
        according to the user, the volume can be set to:
        max/min/numerical value/percentage value/increased/decreased

        @input: list output from intent extractor
    '''

    assert(type(slots) == list)
    assert(len(slots) == 1)

    slot = slots[0]["slotName"]
    value = slots[0]["value"]["value"]

    if slot == "exact":
        setVolume(int(slots[0]["rawValue"]))
    elif slot == "default":
        if value == "up":
            increaseVolume()
        elif value == "max":
            setVolume(100)
        elif value == "min":
            setVolume(0)
        elif value == "mute":
            setVolume(0)
        elif value == "down":
            decreaseVolume()
        elif value.isdigit():
            setVolume(int(value))
        else:
            return cannotDoThatYet()

    NSBeep()

    return


def setVolume(value):
    '''
        set volume of the current output source to a value

        @input: int value of volume
    '''

    osascript.osascript("set volume output volume " + str(value))

    print("Volume has been set to " + str(value))

    return


def getOutputVolume():
    '''
        get output volume of the current output source

        it does not work when the output source is not accessible
        like a monitor with speakers.
    '''

    currentVolume = osascript.osascript("get volume settings")
    # print(currentVolume)
    volumeSetting = currentVolume[1].split(", ")
    # print(volumeSetting)
    output = int(volumeSetting[0].split(":")[1])
    mute = volumeSetting[3].split(":")[1] == "true"

    return output, mute


def increaseVolume():
    '''
        increase volume by 10 from the current output volume
    '''

    output, mute = getOutputVolume()

    if mute:
        setVolume(10)
        return
    if output == 100:
        return

    setVolume(output + 10)
    return


def decreaseVolume():
    '''
        decrease volume by 10 from the current output volume
    '''

    output, mute = getOutputVolume()

    if mute:
        return
    setVolume(output - 10)

    return
