#!/Users/evamy/bot/bin/python
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

# from . import *
import argparse
from interface.speech import talk


parser = argparse.ArgumentParser(description="Extract intent from statement")
parser.add_argument("-c", "--command", type=str,
                    help="write a command for a response")

args = parser.parse_args()

talk.waitForInit()
